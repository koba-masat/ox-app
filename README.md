# README

## 必要なPythonライブラリをインストールする

- pip install -r requirements.txt

## 仮想カメラ用のobs-virtualsource.dllを有効にする

1. コマンドプロンプトを管理者として実行する
2. 以下のコマンドをpullしたディレクトリで実行する
    ```bash
    regsvr32 /n /i:1 "obs-virtualcam\bin\64bit\obs-virtualsource.dll"
    ```
3. PCを再起動

## プログラムを実行する

1. カメラをつけているなら、オフにする
2. 以下のコマンドをpullしたディレクトリで実行する
    ```bash
    python ox-app.py
    ```
3. カメラを選択する際にOBS Virtual Camera にする