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

# Exemplo de uso

s = Student(
    id=uuid4(),
    securityNumber="44069617809",
    firstName="Matheus",
    familyName="de Almeida Cantarutti",
    birthDate="1994-07-20",
    adaiCampus="ADAI - Campestre",
    studentEmail="cantaruttim@outlook.com",
    studentPhone="(11)932045898",
    courseEnrolled="TM16"
)

u = User.from_student(s)

print(u.userName)
print(u.userPassword)
