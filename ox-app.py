import cv2
import pyvirtualcam

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()
with pyvirtualcam.Camera(width=frame.shape[1], height=frame.shape[0], fps=30) as cam:
    print(frame.shape[1])
    while True:
        # 各フレームの画像を取得
        ret, frame = cap.read()

        # ここで何らかのエフェクトをかける

        # 色空間を変更
        # αチャンネルを有効にして，RGB順にする
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        print(frame)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()