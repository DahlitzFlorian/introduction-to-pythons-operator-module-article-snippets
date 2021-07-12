# student_dict.py
import operator

students = (
    ("Albert", "Einstein", 12345),
    ("Richard", "Feynman", 73855),
    ("Isaac", "Newton", 39352),
)

get_last_name = operator.itemgetter(1)
get_id_last_name = operator.itemgetter(2, 1)

sorted_by_last_name = sorted(students, key=get_last_name)
sorted_by_id_last_name = sorted(students, key=get_id_last_name)

print(sorted_by_last_name)
print(sorted_by_id_last_name)
