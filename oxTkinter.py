import tkinter as tk


class Controller:
    mark = ""
    x_offset = 100
    y_offset = 100

    def __init__(self, mark="", x_offset=100, y_offset=100):
        self.mark = mark
        self.x_offset = x_offset
        self.y_offset = y_offset

    def maru(self):
        self.mark = "maru"

    def batsu(self):
        self.mark = "batsu"

    def nashi(self):
        self.mark = ""

    def right(self):
        self.x_offset += 1

    def left(self):
        self.x_offset -= 1

    def up(self):
        self.y_offset -= 1

    def down(self):
        self.y_offset += 1

    def tkButton(self):
        root = tk.Tk()
        root.geometry("300x150")
        maru_button = tk.Button(root, text="まる", command=maru)
        batsu_button = tk.Button(root, text="ばつ", command=batsu)
        nashi_button = tk.Button(root, text="なし", command=nashi)
        right_button = tk.Button(
            root, text="right", command=right, repeatdelay=1, repeatinterval=10)
        left_button = tk.Button(root, text="left", command=left,
                                repeatdelay=1, repeatinterval=10)
        up_button = tk.Button(root, text="up", command=up,
                              repeatdelay=1, repeatinterval=10)
        down_button = tk.Button(root, text="down", command=down,
                                repeatdelay=1, repeatinterval=10)
        maru_button.grid(row=1, column=1, padx=50,
                         pady=5, columnspan=2, rowspan=2)
        batsu_button.grid(row=4, column=1, padx=50,
                          pady=5, columnspan=2, rowspan=2)
        nashi_button.grid(row=6, column=1, padx=50,
                          pady=5, columnspan=2, rowspan=2)
        right_button.grid(row=4, column=10, pady=5, columnspan=2, rowspan=2)
        left_button.grid(row=4, column=6, pady=5, columnspan=2, rowspan=2)
        up_button.grid(row=1, column=8, pady=5, columnspan=2, rowspan=2)
        down_button.grid(row=6, column=8, pady=5, columnspan=2, rowspan=2)
        root.mainloop()

    def mark_chage(self, maru_array, batsu_array):
        if self.mark == "maru":
            return maru_array
        elif self.mark == "batsu":
            return batsu_array

    def can_move(self, frame_shape, mark_shape):
        upper_left = [self.x_offset, self.y_offset]
        lower_right = [self.x_offset + mark_shape[0], self.y_offset + mark_shape[1]]
        upper_left[0] < 0 or upper_left[1] < 0