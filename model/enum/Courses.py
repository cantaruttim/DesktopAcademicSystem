from enum import Enum

class Courses(Enum):
    """
        Class Courses
        Contains all the courses that ADAI College manage

    """
    ADAI_COLLEGE_INTENSIVE= 1
    ADAI_COLLEGE_MASTER= 2
    ADAI_COLLEGE_CORP= 3

print(Courses.ADAI_COLLEGE_INTENSIVE)
print(Courses.ADAI_COLLEGE_INTENSIVE.value)
