class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name:{self.name} Age:{self.age}"

class Student(person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course

    def display(self):
        return f"Name:{self.name},Course:{self.course},Age:{self.age}"

student=Student("alice",30,"Phython")
print(student.display())

