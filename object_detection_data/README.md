# diff_data

- 白黒動画から差分動画を作成する

## 使い方

- combined_data ディレクトリに、結合済みのデータを配置する。
- 仮想環境構築後、`sh environments.sh`を実行すると、必要なライブラリがインストールされます。(venv.md 参照)
- `python3 object_detection.py -m yolox_s.onnx -s 0.3 --input_shape 640,640`を実行すると、`object_detection_data`ディレクトリの各ディレクトリに、動画と csv が出力されます。

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

↓

```

object_detection_data
.
├── environments.sh
├── normal_train
│   ├── fullstream.mp4
│   └── livedata.csv
├── normal_val
│   ├── fullstream.mp4
│   └── livedata.csv
├── object_detection.py
├── README.md
├── requirements.txt
├── venv.md
├── with_info
│   ├── fullstream.mp4
│   └── livedata.csv
├── without_info
│   ├── fullstream.mp4
│   └── livedata.csv
└── yolox_s.onnx


```
