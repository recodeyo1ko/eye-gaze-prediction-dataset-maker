import argparse
import os

import cv2
import numpy as np
import pandas as pd

import onnxruntime
import time
import logging #ログを出力する時のモジュール

from yolox.data.data_augment import preproc as preprocess
from yolox.data.datasets.coco_classes import COCO_CLASSES
from yolox.utils.demo_utils import mkdir, multiclass_nms, demo_postprocess
from yolox.utils.visualize import vis

import shutil

def make_parser(case, input_path):
    parser = argparse.ArgumentParser("onnxruntime inference sample") #ArgumentParserクラスのインスタンスを生成
    #add_argumentメソッドでコマンドライン引数の解析方法を追加
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="yolox.onnx",
        help="Input your onnx model.",
    )
    parser.add_argument(
        "-i",
        "--input_path",
        type=str,
        default=input_path,
        help="Path to your input image.",
    )
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default=case,
        help="Path to your output directory.",
    )
    parser.add_argument(
        "-s",
        "--score_thr",
        type=float,
        default=0.3,
        help="Score threshould to filter the result.",
    )
    parser.add_argument(
        "--input_shape",
        type=str,
        default="640,640",
        help="Specify an input shape for inference.",
    )
    parser.add_argument(
        "--with_p6",
        action="store_true",
        help="Whether your model uses p6 in FPN/PAN.",
    )
    return parser


def visual(origin_img, predictions, ratio, args):
    boxes = predictions[:, :4]
    scores = predictions[:, 4:5] * predictions[:, 5:]
    boxes_xyxy = np.ones_like(boxes)
    boxes_xyxy[:, 0] = boxes[:, 0] - boxes[:, 2] / 2.
    boxes_xyxy[:, 1] = boxes[:, 1] - boxes[:, 3] / 2.
    boxes_xyxy[:, 2] = boxes[:, 0] + boxes[:, 2] / 2.
    boxes_xyxy[:, 3] = boxes[:, 1] + boxes[:, 3] / 2.
    boxes_xyxy /= ratio
    dets = multiclass_nms(boxes_xyxy, scores, nms_thr=0.45, score_thr=0.1)
    
    # Create a mask to preserve the inside of the detected boxes
    mask = np.zeros_like(origin_img)
    final_boxes = []  # Initialize final_boxes as an empty list
    final_scores = []  # Initialize final_scores as an empty list
    final_cls_inds = []  # Initialize final_cls_inds as an empty list
    
    if dets is not None:
        final_boxes, final_scores, final_cls_inds = dets[:, :4], dets[:, 4], dets[:, 5]
        for box in final_boxes:
            x1, y1, x2, y2 = box.astype(int)
            mask[y1:y2, x1:x2] = 1  # Set the region inside the box to 1 (white)
    
    # Apply the mask to the original image
    result_img = origin_img * mask

    return result_img, final_boxes, final_scores, final_cls_inds

def infe_video(args,input_shape): ###
    cap = cv2.VideoCapture(args.input_path)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    output_dir = args.output_dir
    mkdir(output_dir)
    save_path = os.path.join(output_dir,os.path.basename(args.input_path))
    
    vid_writer = cv2.VideoWriter(
            save_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (int(width), int(height))
        )
    logging.info(f'onnx model: {os.path.basename(args.model)}')
    
    ##
    f = 0 #フレーム数の初期値
    while True: #無限ループ
        ret_val, origin_img = cap.read() #画像情報が格納されたらret_valにTrueを代入
        f += 1 #動画のフレーム数
        if ret_val:
            img, ratio = preprocess(origin_img, input_shape)
            ##背景黒画像にする
            #img, ratio = preprocess(origin_img, input_shape)
            
            start = time.time()
            session = onnxruntime.InferenceSession(args.model)
            
            ort_inputs = {session.get_inputs()[0].name: img[None, :, :, :]}
            output = session.run(None, ort_inputs)
            predictions = demo_postprocess(output[0], input_shape, p6=args.with_p6)[0]
            # logging.info(f'Infer time: {time.time()-start:.4f} [s]')
            
            result_img, final_box, final_score, final_cls_ind =visual(origin_img, predictions, ratio, args) #############################################            

            ###物体検出の結果を表形式で出力する。
            result = []
            #[result.extend((final_cls_ind[x],COCO_CLASSES[int(final_cls_ind[x])],final_score[x],final_box[x][0],final_box[x][1],final_box[x][2],final_box[x][3]) for x in range(len(final_score)))]
            #df = pd.DataFrame(result, columns = ['class-id','class','score','x-min','y-min','x-max','y-max'])
            [result.extend((COCO_CLASSES[int(final_cls_ind[x])],int(final_box[x][1]),int(final_box[x][3]),int(final_box[x][0]),int(final_box[x][2]),final_score[x]) for x in range(len(final_score)))]

            #[result.extend((COCO_CLASSES[int(final_cls_ind[x])],final_box[x][1],final_box[x][3],final_box[x][0],final_box[x][2],final_score[x]) for x in range(len(final_score)))]
            df = pd.DataFrame(result, columns= ['class','y-min','y-max','x-min','x-max','score'])
            
            vid_writer.write(result_img)
            
            ch = cv2.waitKey(1)
            if ch == 27 or ch == ord("q") or ch == ord("Q"):
                break
        else: #画像情報が格納されなくなったらループから抜ける。
            break
    
    logging.info(f'save_path: {save_path}')
    logging.info(f'Inference Finish!')

def path(case):
    current_dir = os.getcwd()
    current_dir_path = os.path.dirname(current_dir)
    input_file = os.path.join(current_dir_path + '/combined_data', case, 'fullstream.mp4')
    output_file = os.path.join(current_dir_path + '/object_detection_data', case, 'fullstream.mp4')
    csv_file = os.path.join(current_dir_path + '/combined_data', case, 'livedata.csv')
    csv_copy_file = os.path.join(current_dir_path + '/object_detection_data', case, 'livedata.csv')

    return input_file, output_file, csv_file, csv_copy_file

def copy_csv_file(csv_file, csv_copy_file):
    try:
        shutil.copy(csv_file, csv_copy_file)
        print("CSVファイルのコピーが完了しました。")
    except Exception as e:
        print("CSVファイルのコピー中にエラーが発生しました:", str(e))

def main():

    case = input("input case number; 0:normal_train, 1: normal_val, 2:without_info, 3:with_info  ;")
    if case == '0':
        case = 'normal_train'
    elif case == '1':
        case = 'normal_val'
    elif case == '2':
        case = 'without_info'
    elif case == '3':
        case = 'with_info'
    else:
        print('input error')
        exit()
    input_path, output_path, csv_file, csv_copy_file = path(case)

    args = make_parser(case, input_path).parse_args() #コマンドライン引数の解析
    #出力するログに対して設定を追加する
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s")
    
    #tuple() tuple型に変更。tuple型は要素を変更したり、削除したりすることはできない。
    #map() 
    # 第一引数に適用する関数(呼び出し可能オブジェクト)、第二引数にリストなどのイテラブルオブジェクト
    # map型のオブジェクト(イテレータ)を返す。
    input_shape = tuple(map(int, args.input_shape.split(',')))
    logging.info(f'Input Size: {input_shape}')
    copy_csv_file(csv_file, csv_copy_file)

    infe_video(args,input_shape)
    ###############################################
    
    

#if __name__ == "__main__": があると、モジュールがPythonスクリプトとして起動された場合
# (＊例えばpython ファイル名.py 等にて実行された場合）のみ、if __name__ == “__main__”: 配下の処理が実行されます。
if __name__ == '__main__':
    main()