import math, random
students = []

#  get the students name
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase

# print the student title case
def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

# add student to the list with student id optional
def add_student(name, student_id= None):
    # add random student id if none provided
    if student_id is None:
        student_id =  random.randrange(0, math.pow(2,24)-1)
    student = {"name": name, "student_id": student_id}
    students.append(student)

student_list = get_students_titlecase()

add_student("john")
add_student("john2")
add_student("john3")
add_student("john4")

print(students)