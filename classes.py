import math, random

students =[]

# create class
class Student:
    # contructor
    # self need to be added
    def __init__(self, name, student_id=None):
        # add random student id if none provided
        if student_id is None:
            student_id = random.randrange(0, math.pow(2, 24) - 1)

        # create class var
        self.name = name;
        self.student_id = student_id

        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitize(self):
        return self.name.capitalize()

student_mark = Student("mark")

print(student_mark)