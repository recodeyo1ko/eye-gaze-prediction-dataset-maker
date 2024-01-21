# 視線予測データセットメーカー

- 視線予測で扱うデータを整形します。
- 生データを準備して、使い方に従って順次処理をしてください。
- 基本的には、`/row_data`から順に実行していくことで、データセットが作成されます。
- それぞれのディレクトリには、`README.md`があり、詳細な説明が記載されています。

## 使い方

0. `data` ディレクトリに`recordings`データを配置
1. `/row_data`・・・ディレクトリの名前・構成の整理について
2. `/trimmed_data`・・・データのトリミングについて
3. `/combined_data`・・・データの結合について
4. `/black_and_white_data`・・・動画の白黒化について
5. `/diff_data`・・・差分動画について
6. `/object_detection_data`・・・物体検出について
