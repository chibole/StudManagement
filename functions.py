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
    #     crete a dict
    student = {"name": name, "student_id": student_id}
    # add dict to the list
    students.append(student)


# any number ags
# def var_args(name, *args):
#     print(name)
#     print(args)
#
# def kvar_args(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["id"])

# var_args("test", "user", "new",  True)
# kvar_args("don", description ="user", id ="id_123")

# save list to the file
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


# read from the file
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

# read file is exists
read_file()

student_name = input("Enter a student name: ")
student_id = input("Enter student Id: ")

add_student(student_name, student_id)
# call to save
save_file(student_name)

print(students)
