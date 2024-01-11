import shutil
import cv2
import os

def path(case):
    current_dir = os.getcwd()
    current_dir_path = os.path.dirname(current_dir)
    input_file = os.path.join(current_dir_path + '/combined_data', case, 'fullstream.mp4')
    output_file = os.path.join(current_dir_path + '/black_and_white_data', case, 'fullstream.mp4')
    csv_file = os.path.join(current_dir_path + '/combined_data', case, 'livedata.csv')
    csv_copy_file = os.path.join(current_dir_path + '/black_and_white_data', case, 'livedata.csv')

    return input_file, output_file, csv_file, csv_copy_file

def copy_csv_file(csv_file, csv_copy_file):
    try:
        shutil.copy(csv_file, csv_copy_file)
        print("CSVファイルのコピーが完了しました。")
    except Exception as e:
        print("CSVファイルのコピー中にエラーが発生しました:", str(e))

def movie_from_color_to_black_and_white(input_file, output_file):
    cap = cv2.VideoCapture(input_file)

    # 出力ビデオの設定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
    fps = int(cap.get(5))
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR))

    cap.release()
    out.release()

    print("映像をカラーから白黒に変換が完了しました。")


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
    movie_from_color_to_black_and_white(input_path, output_path)
    copy_csv_file(csv_file, csv_copy_file)

if __name__ == "__main__":
    main()