# student_class.py
import operator


class Student:
    def __init__(self, first_name: str, last_name: str, student_id: int) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.student_id: str = student_id
    
    def __repr__(self) -> str:
        return f"Student(first_name={self.first_name}, last_name={self.last_name}, student_id={self.student_id})"


students = [
    Student("Albert", "Einstein", 12345),
    Student("Richard", "Feynman", 73855),
    Student("Isaac", "Newton", 39352),
]

get_last_name = operator.attrgetter("last_name")
get_id_last_name = operator.attrgetter("student_id", "last_name")

sorted_by_last_name = sorted(students, key=get_last_name)
sorted_by_id_last_name = sorted(students, key=get_id_last_name)

print(sorted_by_last_name)
print(sorted_by_id_last_name)
