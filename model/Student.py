from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Student:
    securityNumber: str
    firstName: str
    familyName: str
    birthDate: str
    adaiCampus: str
    studentEmail: str
    studentPhone: str
    courseEnrolled: str
    id: UUID = field(default_factory=uuid4)