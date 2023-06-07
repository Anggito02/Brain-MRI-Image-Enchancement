from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import subprocess

from WindowTemplate import InitWindow

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png")])

    # close current window
    root_window.get_window().destroy()

    # open new window
    subprocess.run(["python", "views\\image.py", file_path])

def show_window(root_window: Tk, window_size: tuple):

    # Center pos
    center_x = int(window_size[0] / 2)
    center_y = int(window_size[1] / 2)

    # Create 2 buttons
    btn_input = ttk.Button(root_window, text="Input MRI Image", width=20, command=select_image)

    # Show buttons
    btn_input.place(x=center_x, y=center_y, anchor="center")

if __name__ == "__main__":
    root_window = InitWindow()
    root_window.set_size((300, 200))
    root_window.set_resizeable(False)
    root_window.set_title("Input")
    show_window(root_window.get_window(), (300, 200))
    root_window.get_window().mainloop()