import cv2
import pyvirtualcam
import numpy as np
import threading as th

# import ox-tkinter
from oxTkinter import Controller

# 取得するデータソース（Webカメラ）を選択
cap = cv2.VideoCapture(0)
# 最初のフレームから画像のサイズを取得
ret, frame = cap.read()

controller = Controller()

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

        marubatsu_array = controller.mark_chage(maru_array, batsu_array)
        # print(controller.mark)

        if controller.mark == "maru" or controller.mark == "batsu":
            if controller.can_move([frame.shape[0], frame.shape[1]],
                                [marubatsu_array.shape[0], marubatsu_array.shape[1]]):
                                
                frame[controller.y_offset: controller.y_offset + marubatsu_array.shape[0],
                    controller.x_offset: controller.x_offset + marubatsu_array.shape[1]] = marubatsu_array

        frame = np.flip(frame, 2)
        # 画像を仮想カメラに流す
        cam.send(frame)

        # 画像をスクリーンに表示しなくなったので，pyvirtualcamの機能を使って次のフレームまで待機する
        cam.sleep_until_next_frame()

# 終了処理
cap.release()
