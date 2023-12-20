# original-data の numbering.py について

# 背景

- 取得後データの階層と名前がぐちゃぐちゃなので、整理する

# 前提

- 取得データ（`recordings`）は、`original-data`ディレクトリに配置する

```
└── recordings
    ├── ランダムなディレクトリ名
    │   ├── (省略)
    │   ├── segments
    │   │   └── 1
    │   │       ├── (省略)
    │   │       ├── fullstream.mp4
    │   │       ├── livedata.json.gz
    │   │       ├── (省略)
    │   └── (省略)
(省略)
```

↓

```
└── recordings
    ├── 1
    │   ├── fullstream.mp4
    │   └── livedata.json.gz
    ├── 2
    │   ├── fullstream.mp4
    │   └── livedata.json.gz
    (省略)
```
