class Shape:
    def _init_(self, colour):
        self.colour = colour

class Rectangle(Shape):
    def _init_(self, colour, length, width):
        super()._init_(colour)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

colour = input("Enter the colour of the rectangle: ")
length = int(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle=Rectangle(colour, length, width)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()


print(f"The colour of the rectangle is {rectangle.colour}.")
print(f"The area of the rectangle is {area}.")
print(f"The perimeter of the rectangle is {perimeter}.")