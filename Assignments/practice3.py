# ADDITIONAL OPERATOR
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Add the arrays 
result = array1 + array2
print(result)

# SUBTRACTION OPERATOR
import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Subtract the arrays 
result = array1 - array2
print(result)

# Multiplication OPERATOR
import numpy as np
array = np.array([[1, 2], [3, 4]])

# Multiply the array 
result = array * 2
print(result)

# Division OPERATOR
import numpy as np
array = np.array([[2, 4], [6, 8]])

result = array / 2
print(result)


# Matrix multiplication operator

import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result = np.dot(array1, array2)
print(result)


# HOW TO IMPLEMENT A SWITCH-CASE IN 2D ARRAYS 
def case1():
    print("This is case 1")

def case2():
    print("This is case 2")

def case3():
    print("This is case 3")

switch = {
    1: case1,
    2: case2,
    3: case3
}