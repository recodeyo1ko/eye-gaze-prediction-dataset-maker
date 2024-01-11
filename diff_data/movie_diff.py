import shutil
import cv2
import os
import numpy as np

def path(case):
    current_dir = os.getcwd()
    current_dir_path = os.path.dirname(current_dir)
    input_file = os.path.join(current_dir_path + '/black_and_white_data', case, 'fullstream.mp4')
    output_file = os.path.join(current_dir_path + '/diff_data', case, 'fullstream.mp4')
    csv_file = os.path.join(current_dir_path + '/black_and_white_data', case, 'livedata.csv')
    csv_copy_file = os.path.join(current_dir_path + '/diff_data', case, 'livedata.csv')
    diff_frame_num = 2
    return input_file, output_file, csv_file, csv_copy_file, diff_frame_num

def movie_diff(input_file, output_file, diff_frame_num):
    cap = cv2.VideoCapture(input_file)
    # 出力ビデオの設定
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(5))
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    prev_frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if len(prev_frames) < diff_frame_num:
            out.write(frame)
        # 差分を計算
        if len(prev_frames) == diff_frame_num:
            frame_diff = np.zeros_like(gray_frame, dtype=np.uint8)
            for prev_frame in prev_frames:
                frame_diff = cv2.bitwise_or(frame_diff, cv2.absdiff(prev_frame, gray_frame))
            # フレームを出力ビデオに書き込む
            out.write(cv2.cvtColor(frame_diff, cv2.COLOR_GRAY2BGR))
        # 現在のフレームを前のフレームとして保存
        prev_frames.append(gray_frame)
        if len(prev_frames) > diff_frame_num:
            prev_frames.pop(0)
    cap.release()
    out.release()
    print("差分映像の生成が完了しました。")

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
    input_path, output__path, csv_file, csv_copy_file, diff_frame_num = path(case)
    movie_diff(input_path, output__path, diff_frame_num)
    copy_csv_file(csv_file, csv_copy_file)

if __name__ == "__main__":
    main()