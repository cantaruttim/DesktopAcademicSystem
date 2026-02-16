from tkinter import ttk

from model.Student import Student


class RegisterPage(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="Register Student", font=("Arial", 20))
        label.pack(pady=20)

        back_button = ttk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame("HomePage")
        )
        back_button.pack()

        form_frame = ttk.Frame(self)
        form_frame.pack(pady=10, padx=10)

        self.securityNumber = ttk.Entry(form_frame)
        self.firstName = ttk.Entry(form_frame)
        self.familyName = ttk.Entry(form_frame)
        self.birthDate = ttk.Entry(form_frame)
        self.adaiCampus = ttk.Entry(form_frame)
        self.studentEmail = ttk.Entry(form_frame)
        self.studentPhone = ttk.Entry(form_frame)
        self.courseEnrolled = ttk.Entry(form_frame)

        # Labels + Entries
        fields = [
            ("Security Number", self.securityNumber),
            ("First Name", self.firstName),
            ("Family Name", self.familyName),
            ("Birth Date", self.birthDate),
            ("Campus", self.adaiCampus),
            ("Email", self.studentEmail),
            ("Phone", self.studentPhone),
            ("Course", self.courseEnrolled),
        ]

        for i, (label_text, entry) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="w", pady=2)
            entry.grid(row=i, column=1, pady=2)

        # ttk.Button(
        #     self,
        #     text="Save Student",
        #     command=self.save_student
        # ).pack(pady=10)

        ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame("HomePage")
        ).pack()


