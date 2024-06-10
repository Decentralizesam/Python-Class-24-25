
           


           #create class called Animal should have a Dogname 
           #method called bark 
           #object called dog and make it dynamic 
           #return dog name and bark as a string


class Animal:
    def __init__(self, dogname):
        self.Dogname = dogname

    def Character(self):
        return f"A Barking Dog {self.Dogname}"

Dogname=input("Enter the Dog name :")

dog=Animal(Dogname)

print(dog.Character())


