# black_and_white_data

- 動画を白黒化する

## 使い方

- combined_data ディレクトリに、結合済みのデータを配置する。

```

combined_data
├── combine.py
├── normal
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

- `movie_from_color_to_black_and_white.py`を実行すると、`black_and_white_data`ディレクトリに白黒化した動画が配置されます。

↓

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
