from tkinter import *
from tkinter import ttk
from PIL import Image

import sys

from WindowTemplate import InitWindow

def resize_image(image_path, new_size):
    img = Image.open(image_path)
    resized_img = img.resize(new_size, Image.LANCZOS)
    return resized_img

def show_window(root_window: Tk, window_size: tuple, file_location: str):

    # Center pos
    center_x = int(window_size[0] / 2)
    center_y = int(window_size[1] / 2)

    # Create label
    lbl_image = ttk.Label(root_window, text="Your Image")
    lbl_image.place(x=center_x, y=center_y, anchor="center")

    # Resize image
    img = resize_image(file_location, (500, 500))

    # Create image
    img = PhotoImage(file=file_location)
    lbl_image.config(image=img)
    lbl_image.image = img

    # Create button
    btn_process = ttk.Button(root_window, text="Process", width=20)

    # Set button in the bottom
    btn_process.place(x=center_x, y=window_size[1] - 50, anchor="center")

if __name__ == "__main__":
    file_location = sys.argv[1]
    print(file_location)

    root_window = InitWindow()
    root_window.set_size((600, 600))
    root_window.set_resizeable(False)
    root_window.set_title("Your Image")
    show_window(root_window.get_window(), (600, 600), file_location)
    root_window.get_window().mainloop()