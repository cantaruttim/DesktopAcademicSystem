from tkinter import ttk
from ui.container import RegisterPage

class HomePage(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="Home Page", font=("Arial", 20))
        label.pack(pady=20)

        go_button = ttk.Button(
            self,
            text="Go to Register",
            command=lambda: controller.show_frame(RegisterPage)
        )
        go_button.pack()
