
#create class called Animal should have a Dogname 
#method called bark 
#object called dog and make it dynamic 
#return dog name and bark as a string





class cat:
    def __init__(self,name):
        self.name = name

    def behaviors(self):
        return f"A pretty cat : {self.name}"

name=input("Enter the name of the cat :")

character=behaviors()
print(character)