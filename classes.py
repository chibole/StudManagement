import math, random

students =[]

# create class
class Student:
    # self need to be added
    def add_student(self, name, student_id=None):
        # add random student id if none provided
        if student_id is None:
            student_id = random.randrange(0, math.pow(2, 24) - 1)
        #     crete a dict
        student = {"name": name, "student_id": student_id}
        # add dict to the list
        students.append(student)

student = Student()
student.add_student("mark")

print(students)