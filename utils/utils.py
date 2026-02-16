from model.Student import Student
from datetime import datetime

def defaultUserName(s: Student):
    """
        Creates a default registration number for the student
        Parameters:
            s: A Student instance of the Student class
    """

    lastFourDigits = s.securityNumber[-4:]
    currentYear = datetime.now().year
    courseEnrolled = s.courseEnrolled
    courseEnrolledSplit = courseEnrolled[:2]

    return f"{currentYear}{lastFourDigits}{courseEnrolledSplit}"

def defaultPassword(s : Student):
    """
        Creates a default password for the student
        Parameters:
            s: A Student instance of the Student class
    """

    currentYear = datetime.now().year
    currentMonth = f"{datetime.now().month:02d}"
    courseEnrolled = s.courseEnrolled
    courseEnrolledSplit = courseEnrolled[:2]
    lastFourRegistrationNumberDigits = s.securityNumber[-4:]

    if courseEnrolledSplit not in (["TI", "TM", "TC"]):
        print("Course not found!")

    return str(currentYear) + courseEnrolledSplit + currentMonth + lastFourRegistrationNumberDigits