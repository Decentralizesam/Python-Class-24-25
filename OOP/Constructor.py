# Constructor is a special methdo that is called when an object is created
#purpose of a construc tor 
# it is used to intialize the object's attributes
#the name of this method is "__init__()"
# name : __init__
# fisrt parameter : self
# other parameters : param1...............param_no


class person1:
    def __init__(self,name,age): # Constructor 
        self.name = name
        self.age = age           # instance(Objects)of a class person(An object is an instance of a class)# class is a blueprint of which objects are created 

object = person1("Alice",20)# this is a person class Constructor
# the constructor can not be empty because we have parameters in the constructor
print(f"Name: {object.name}age: {object.age}")



# Constructor with no parameters

class person2:
    def __init__(self):
        self.name = "unknown" 
        self.age =0

object = person2()
print(f"Name:{object.name} - Age {object.name}")



class person3:
    params="constructor with no parameters"


object=person3()
print(object.params)








