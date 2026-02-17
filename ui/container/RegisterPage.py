from tkinter import ttk
import os
from model.Student import Student
from model.User import User

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
        self.courseEnrolled = (
            ttk.Combobox(
                form_frame,
                values=["COLLEGE INTENSIVO", "COLLEGE MASTER", "COLLEGE CORP"],
                state="readonly")
        )
        self.courseEnrolled.set("Select Course")

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

        ttk.Button(
            self,
            text="Save Student",
            command=self.save_student
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame("HomePage")
        ).pack()

    def save_student(self):
        student = Student(
            securityNumber=self.securityNumber.get(),
            firstName=self.firstName.get(),
            familyName=self.familyName.get(),
            birthDate=self.birthDate.get(),
            adaiCampus=self.adaiCampus.get(),
            studentEmail=self.studentEmail.get(),
            studentPhone=self.studentPhone.get(),
            courseEnrolled=self.courseEnrolled.get(),
        )

        user = User.from_student(student)
        self.save_to_file(student, user)

        print("Student and User saved successfully!")

    def save_to_file(self, student, user):
        file_path = "students.txt"

        with open(file_path, "a", encoding="utf-8") as file:
            file.write("=== STUDENT ===\n")
            file.write(f"ID: {student.id}\n")
            file.write(f"Security Number: {student.securityNumber}\n")
            file.write(f"Name: {student.firstName} {student.familyName}\n")
            file.write(f"Birth Date: {student.birthDate}\n")
            file.write(f"Campus: {student.adaiCampus}\n")
            file.write(f"Email: {student.studentEmail}\n")
            file.write(f"Phone: {student.studentPhone}\n")
            file.write(f"Course: {student.courseEnrolled}\n")

            file.write("\n--- USER ---\n")
            file.write(f"User ID (same as student): {user.id}\n")
            file.write(f"Username: {user.userName}\n")
            file.write(f"Password: {user.userPassword}\n")
            file.write("\n=============================\n\n")
