## Python 環境構築

## はじめに

### 仮想環境の構築

- 仮想環を用意できていない場合には仮想環境をまず作成しておく。

```bash
python3 -m venv env
```

- 仮想環境の有効化

```bash
#Windowsの場合
env\scripts\activate.bat
#Mac/Ubuntuの場合
source env/bin/activate
```

- 仮想環境のライブラリのインストール
  - 一行ずつ実行する場合は最下部参考
  - ある程度 sh でまとめてあるので、それを実行する場合は以下を実行(必ず仮想環境が立ち上がっていることを確認してから)

```bash
sh environments.sh
```

この後

仮想環境の無効化

```bash
deactivate
```

## memo

```bash
ライブラリの出力
pip3 list
ライブラリの保存
pip3  freeze > requirements.txt
```

### [補足]ライブラリのインストール

```bash
pip3 install --upgrade pip
pip3 install tensorflow
pip3 install matplotlib
pip3 install opencv-python
pip3 install pydot
pip3 install pydotplus
pip3 install pandas
pip3 install onnx
pip3 install onnxruntime

## graphvizのインストールだけはpipではダメらしい
apt-get install graphviz
### これがエラーになる
pip3 install yolox
```

### 追加

```bash
git clone git@github.com:Megvii-BaseDetection/YOLOX.git
cd YOLOX
pip install -U pip
pip install -r requirements.txt
pip3 install -v -e .


```

### [Issue]

`bad interpreter: No such file or directory` が出た場合には、`rm -rf env` で仮想環境を削除して、再度作成する。
