# diff_data

- 白黒動画から差分動画を作成する

## 使い方

- black_and_white_data ディレクトリに、白黒化した動画を配置する。csv ファイルも同時に配置する。

```

black_and_white_data
├── movie_from_color_to_black_and_white.py
├── normal_train
│   ├── fullstream.mp4
│   └── livedata.csv
├── normal_val
│   ├── fullstream.mp4
│   └── livedata.csv
├── README.md
├── with_info
│   ├── fullstream.mp4
│   └── livedata.csv
└── without_info
    ├── fullstream.mp4
    └── livedata.csv

```

- `movie_diff.py`を実行すると、`diff_data`ディレクトリに差分動画が配置されます。

↓

```

diff_data
├── movie_diff.py
├── normal_train
│   ├── fullstream.mp4
│   └── livedata.csv
├── normal_val
│   ├── fullstream.mp4
│   └── livedata.csv
├── README.md
├── with_info
│   ├── fullstream.mp4
│   └── livedata.csv
└── without_info
    ├── fullstream.mp4
    └── livedata.csv

```
