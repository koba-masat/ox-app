import cv2
import pyvirtualcam
import numpy as np
import tkinter as tk

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()
with pyvirtualcam.Camera(width=frame.shape[1], height=frame.shape[0], fps=30) as cam:
    maru_array = cv2.imread("figure/mark_maru.png")
    batsu_array = cv2.imread("figure/mark_batsu.png")
    maru_array = cv2.resize(maru_array, dsize=(100,100))
    batsu_array = cv2.resize(batsu_array, dsize=(100,100))


    root = tk.Tk()
    root.geometry("350x100")

    root.mainloop() 
    while True:
        # 各フレームの画像を取得
        ret, frame = cap.read()

        x_offset = int((frame.shape[1]-maru_array.shape[1])/2)
        y_offset = 80

        frame[y_offset: y_offset+ maru_array.shape[0], x_offset: x_offset+ maru_array.shape[1]] = maru_array
        frame = np.flip(frame,2)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()
