from student import Student

# inherited from Student
class HighSchoolStudent(Student):
    school_name = "abc high school"

    def get_school_name(self):
        return self.school_name + " student"

    # call parent class method
    def get_name_capitize(self):
        original_value = super().get_name_capitize()
        return  original_value + " -sd"
