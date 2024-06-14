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




class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return F"Name:{self.name},Age:{self.age}"

Class Dog(Animal):
def __init__(self,name,age,breed):
    super().__init__(name,age) # super allows the class to initialise the atrributes 
                               #__init__ allows us to initialize the attributes of a class(it is known as a constructor)
    self.breed=breed           # allows us to acesss attributes,methods and variable 
    

    def display(self):
        return f"Name:{self.name},Age:{self.age},breed :{self.breed}"

character=Dog("Alex",30,"dog")
print(dog.display)

