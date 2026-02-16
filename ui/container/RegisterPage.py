from tkinter import ttk
from ui.container import HomePage

class RegisterPage(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="Register Student", font=("Arial", 20))
        label.pack(pady=20)

        back_button = ttk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame(HomePage)
        )
        back_button.pack()
