# original-data の numbering.py について

- 取得データを連番のディレクトリに移動・不要ファイルの削除をします。

## 使い方

- 取得データ（`recordings`）を、`row-data`ディレクトリに配置する。
- json.gz は手動で展開する。

```
row-data
    └── recordings
        ├── ランダムなディレクトリ名
        │   ├── (省略)
        │   ├── segments
        │   │   └── 1
        │   │       ├── (省略)
        │   │       ├── fullstream.mp4
        │   │       ├── livedata.json
        │   │       ├── livedata.json.gz
        │   │       ├── (省略)
        │   └── (省略)
    (省略)
```

- `numbering.py`を実行すると、`recordings`ディレクトリにあるデータが、`1`から始まる連番のディレクトリに変更されます。

↓

```

recordings
    ├── 1
    │ ├── fullstream.mp4
    │ ├── livedata.json
    │ └── livedata.json.gz
    ├── 2
    │ ├── fullstream.mp4
    │ ├── livedata.json
    │ └── livedata.json.gz
    (省略)

```

- `nomal`,`with_info`,`without_info`に分けてデータを分割する。
- 各フォルダの中身は１から始まる連番のディレクトリにする。必要であれば適宜名前を変更する。
