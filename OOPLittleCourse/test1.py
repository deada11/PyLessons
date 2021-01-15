class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = "{0}{1}{2}".format(str(list(self.name)[0]), self.last_name, self.birth_year)


my_student = Student(input(), input(), str(input()))
print(my_student.id)