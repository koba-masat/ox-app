import cv2
import pyvirtualcam
import numpy as np
import tkinter as tk
import threading as th

# import ox-tkinter
from oxTkinter import Controller

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()

mark = "baaaatsu"
x_offset = 100
y_offset = 100
controller = Controller(mark, x_offset, y_offset)

thread1 = th.Thread(target=controller.tkButton)
thread1.start()

with pyvirtualcam.Camera(width=frame.shape[1], height=frame.shape[0], fps=30) as cam:
    maru_array = cv2.imread("figure/mark_maru.png")
    batsu_array = cv2.imread("figure/mark_batsu.png")
    maru_array = cv2.resize(maru_array, dsize=(100, 100))
    batsu_array = cv2.resize(batsu_array, dsize=(100, 100))

    while True:
        # 各フレームの画像を取得
        ret, frame = cap.read()

        if mark == "maru":
            marubatsu_array = maru_array
        elif mark == "batsu":
            marubatsu_array = batsu_array

        if mark == "maru" or mark == "batsu":
            if x_offset < 0:
                x_offset = 0
            if x_offset+marubatsu_array.shape[1] > frame.shape[1]:
                x_offset = frame.shape[1] - marubatsu_array.shape[1]
            if y_offset < 0:
                y_offset = 0
            if y_offset+marubatsu_array.shape[0] > frame.shape[0]:
                y_offset = frame.shape[0] - marubatsu_array.shape[0]
            frame[y_offset: y_offset + marubatsu_array.shape[0],
                  x_offset: x_offset + marubatsu_array.shape[1]] = marubatsu_array

        frame = np.flip(frame, 2)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()
