# combined_data

- トリミング済みのデータを結合する。

## 使い方

- trimmed_data ディレクトリに、トリミング済みのデータを配置する。

```
trimmed_data
  ├── normal
  |   ├── 1
  |   │   ├── fullstream.mp4
  |   │   └── livedata.json
  |   ├── 2
  |   │   ├── fullstream.mp4
  |   │   └── livedata.json
  |   ├── ...
  ├── with_info
  |   ├── 1
  |   │   ├── fullstream.mp4
  |   │   ├── livedata.json
  |   ├── 2
  |   │   ├── fullstream.mp4
  |   │   └── livedata.json
  |   ├── ...
  └── without_info
      ├── 1
      │   ├── fullstream.mp4
      │   └── livedata.json
      ├── 2
      │   ├── fullstream.mp4
      │   └── livedata.json
      ├── ...

```

- `combine.py`を実行すると、`combined_data`ディレクトリに結合後のデータが配置されます。

↓

```

combined_data
  ├── normal
  |   ├── fullstream.mp4
  |   └── livedata.json
  ├── with_info
  |   ├── fullstream.mp4
  |   └── livedata.json
  └── without_info
      ├── fullstream.mp4
      └── livedata.json

```

- 必要に応じて、trimmed_data を２つに分割し、出力される normal を normal_train と normal_val に分割してください。
