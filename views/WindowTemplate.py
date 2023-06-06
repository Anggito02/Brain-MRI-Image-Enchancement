import tkinter as tk

class InitWindow:
    def __init__(self) -> None:
        self.root_window = tk.Tk()

    def get_window(self) -> tk.Tk:
        return self.root_window

    def set_size(self, size: tuple) -> None:
        screen_width = self.root_window.winfo_screenwidth()
        screen_height = self.root_window.winfo_screenheight()

        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2)

        self.root_window.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def set_resizeable(self, resizeable: bool) -> None:
        self.root_window.resizable(resizeable, resizeable)

    def set_title(self, title: str) -> None:
        self.root_window.title(title)