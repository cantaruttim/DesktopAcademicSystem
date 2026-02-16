import tkinter as tk
from tkinter import ttk
from ui.container.HomePage import HomePage
from ui.container.RegisterPage import RegisterPage

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Student System")
        self.geometry("600x400")

        # Container principal
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HomePage, RegisterPage):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

