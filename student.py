import math, random

students =[]

# create class
class Student:
    # class var
    school_name = "abc elementary"

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

    # capitalize the name
    def get_name_capitize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
