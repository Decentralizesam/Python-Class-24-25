class MyClass:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name
        
    def full_name(self):
         print(f"{self.first_name} {self.second_name}")

first_name=input("First Name : ")
second_name=input("Second Name :")

# object creation(instantiation)

obj=MyClass(first_name,second_name)
obj2=MyClass("Mary","jane")

obj.full_name()
obj2.full_name()

class MyStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

def student(self):
    print(f"{self.name} {self.age}")

name=input("Name : ")
age=input("Age : ")

obj=MyStudent(name,age)

obj.student()











