# Code examples of function arguments and parameters

# - Code example function Arguments
# EXAMPLE 1
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

# Output: Sum: 5

# EXAMPLE 2
def number_of_pupils(x, y):
    multiplication = x * y
    print('Total:', multiplication)

    number_of_pupils(170, 30)

    # Output: Total: 5100



# - Code example function Parameters
def greet(name:str):  
    print ('Hello ', name)

greet('Steve') 
greet(123) 


# EXAMPLE 2

def greet(name1, name2, name3):  
    print ('Hello ', name1, ' , ', name2 , ', and ', name3)

greet('Steve', 'Bill', 'Yash') # calling function with string argument