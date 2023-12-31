# trimmed_data

- 動画上の開始と終了の秒数を指定することでトリミングする。
- 対応する時間で json ファイルもトリミングし、csv ファイルに変換する。

## 使い方

- row-data /`nomal`,`with_info`,`without_info`に、それぞれのデータを配置する。

```
row_data
  ├── nomal
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
  |   │   └── livedata.json
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

- `numbering.py`を実行すると、`trimmed_data`ディレクトリの`nomal`,`with_info`,`without_info`ディレクトリにトリミング後のデータが配置されます。

↓

```

trimmed_data
  ├── nomal
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
  |   │   └── livedata.json
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
