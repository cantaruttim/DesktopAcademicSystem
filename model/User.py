from uuid import UUID, uuid4
from dataclasses import dataclass
from model.Student import Student
from utils.utils import defaultUserName, defaultPassword

@dataclass
class User:
    id: UUID
    userName: str
    userPassword: str

    @classmethod
    def from_student(cls, student: Student):
        return cls(
            id=student.id,
            userName=defaultUserName(student),
            userPassword=defaultPassword(student)
        )
