import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Student System")
        self.geometry("600x400")

        # Container principal
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Registrar telas
        for F in (HomePage, RegisterPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
