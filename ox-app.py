import cv2
import pyvirtualcam
import numpy as np
import tkinter as tk
import threading as th

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()

mark = "baaaatsu"
x_offset = 100
y_offset = 100


def maru():
    global mark
    mark = "maru"


def batsu():
    global mark
    mark = "batsu"


def nashi():
    global mark
    mark = ""


def right():
    global x_offset
    x_offset += 1


def left():
    global x_offset
    x_offset -= 1


def up():
    global y_offset
    y_offset -= 1


def down():
    global y_offset
    y_offset += 1


def tkButton():
    root = tk.Tk()
    root.geometry("350x100")
    maru_button = tk.Button(root, text="まる", command=maru)
    batsu_button = tk.Button(root, text="ばつ", command=batsu)
    nashi_button = tk.Button(root, text="なし", command=nashi)
    right_button = tk.Button(root, text="right", command=right, repeatdelay=1, repeatinterval=10)
    left_button = tk.Button(root, text="left", command=left, repeatdelay=1, repeatinterval=10)
    up_button = tk.Button(root, text="up", command=up, repeatdelay=1, repeatinterval=10)
    down_button = tk.Button(root, text="down", command=down, repeatdelay=1, repeatinterval=10)
    maru_button.pack()
    batsu_button.pack()
    nashi_button.pack()
    right_button.pack()
    left_button.pack()
    up_button.pack()
    down_button.pack()
    root.mainloop()


thread1 = th.Thread(target=tkButton)
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
            # x_offset = int((frame.shape[1]-marubatsu_array.shape[1])/2)
            # y_offset = 80
            frame[y_offset: y_offset + marubatsu_array.shape[0],
                  x_offset: x_offset + marubatsu_array.shape[1]] = marubatsu_array
        elif mark == "batsu":
            marubatsu_array = batsu_array
            # x_offset = int((frame.shape[1]-marubatsu_array.shape[1])/2)
            # y_offset = 80
            frame[y_offset: y_offset + marubatsu_array.shape[0],
                  x_offset: x_offset + marubatsu_array.shape[1]] = marubatsu_array

        frame = np.flip(frame, 2)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()
