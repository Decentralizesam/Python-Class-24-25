class livingbeing:
    def __init__(self,name):
        self.name=name

#Intermediate class
class Animal(livingbeing):
    def __init__(self,name,species):
        super().__init__(name)
        self.species=species

#Derived class

class Dog(Animal):
    def __init__(self,name,species,breed):
        super().__init__(name,species)
        self.breed=breed

    def details(self):
        return f"Name : {self.name} species:{self.species} breed:{self.breed}"
## creating an instance of a dog 
dog=Dog("Alex","Canine","Gerzman-shepard")
print(dog.details())
