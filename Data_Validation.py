from pydantic import BaseModel

class student(BaseModel):
    name: str
    age: int
    percentage: float

student_info = {"name": "Raju", "age": 20.5, "percentage": 59}

student = student(**student_info)
print(student.name, student.age, student.percentage, sep=f"\n")