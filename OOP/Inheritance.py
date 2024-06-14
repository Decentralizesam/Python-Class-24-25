class Animal:
    
        def speak(self):
            return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Dog barks"


class Cat(Animal):
    def meows(self):
        return "A cat meows"

dog=Dog()
cat=Cat()

print(dog.speak())
print(dog.bark())

print(cat.speak())
print(cat.meows())




class person:

    def character (self):
        return "A person speaks"
# parent class


# child class inherites from the parant class (person)
class boy(Person):
    def speaks(self):
        return "A man speaks"

class girl(Person):
    def walks(self):
        return "A girl speaks"

boy=boy()
girl=girl()

print(boy.speaks())
print(girl.walks())
    
