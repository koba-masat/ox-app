import cv2
import pyvirtualcam
import numpy as np
import tkinter as tk
import threading as th

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()


def tkButton():
    root = tk.Tk()

    root.geometry("350x100")
    root.mainloop()


thread1 = th.Thread(target=tkButton)
thread1.start()

with pyvirtualcam.Camera(width=frame.shape[1], height=frame.shape[0], fps=30) as cam:
    maru_array = cv2.imread("figure/mark_maru.png")
    batsu_array = cv2.imread("figure/mark_batsu.png")


    if not marubatsu_array:
        marubatsu_array = cv2.resize(marubatsu_array, dsize=(100, 100))

    while True:
        # 各フレームの画像を取得
        ret, frame = cap.read()

        if mark == "maru":
            marubatsu_array = maru_array
            x_offset = int((frame.shape[1]-marubatsu_array.shape[1])/2)
            y_offset = 80

        frame[y_offset: y_offset + marubatsu_array.shape[0],
              x_offset: x_offset + marubatsu_array.shape[1]] = marubatsu_array
        elif mark == "batsu":
            marubatsu_array = batsu_array
            x_offset = int((frame.shape[1]-marubatsu_array.shape[1])/2)
            y_offset = 80

        frame[y_offset: y_offset + marubatsu_array.shape[0],
              x_offset: x_offset + marubatsu_array.shape[1]] = marubatsu_array
        else:
            marubatsu_array =


        frame = np.flip(frame, 2)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()
