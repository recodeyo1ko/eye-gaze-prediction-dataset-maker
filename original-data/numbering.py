import os
import shutil

def move_files_and_delete_segments(folder_path, target_files):
    #指定されたファイルを移動し、segments フォルダを削除する

    # リネーム後のフォルダ（元ランダム文字列フォルダ）と同じ階層のファイルを削除
    for filename in os.listdir(folder_path):
      file_path = os.path.join(folder_path, filename)
      if os.path.isfile(file_path):
          os.remove(file_path)

    segments_path = os.path.join(folder_path, 'segments/1')
    if os.path.exists(segments_path):
        # ファイルを移動
        for filename in target_files:
            src = os.path.join(segments_path, filename)
            if os.path.exists(src):
                shutil.move(src, folder_path)
                print(f"Moved: {src} to {folder_path}")

        # segments フォルダを削除
        shutil.rmtree(os.path.join(folder_path, 'segments'))
        print(f"Deleted segments folder in {folder_path}")

def rename_subfolders_and_cleanup(root_folder, target_files):
    # サブフォルダをリネームし、指定されたファイルを移動してsegmentsを削除

    # サブフォルダの取得
    subfolders = [f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))]
    subfolders.sort()
    
    for i, folder in enumerate(subfolders, start=1):
        original_path = os.path.join(root_folder, folder)
        new_path = os.path.join(root_folder, str(i))
        os.rename(original_path, new_path)
        print(f"Renamed: {original_path} to {new_path}")

        # ファイルの移動とsegmentsの削除
        move_files_and_delete_segments(new_path, target_files)

root_folder = 'recordings/'  # ルートフォルダのパス
target_files = ['fullstream.mp4', 'livedata.json.gz']  # 移動するファイル

rename_subfolders_and_cleanup(root_folder, target_files)
