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
