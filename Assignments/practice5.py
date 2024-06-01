#Assignment 6
      # write functions taking in name ,age ,course
       #call this funtion into another function 
       #functions (registration , profile)

       #when i call profile i should be able to print the name age and course
      # call registration inside the function

def registration():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")
    return name, age, course

def profile():
    name, age, course = registration()
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Test the profile function
profile()
