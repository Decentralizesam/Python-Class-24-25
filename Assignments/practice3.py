#1. Accessing an Element: 
# Create a 2D array
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Access element at row 1, column 2 (0-based indexing)
element = matrix[1][2]
print(element)  # Output: 6


#2. *Adding Two Matrices*:

# Create two matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8, 9],
           [10, 11, 12]]

# Initialize result matrix
result = [[0, 0, 0],
          [0, 0, 0]]

# Add corresponding elements
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(result)  # Output: [[8, 10, 12], [14, 16, 18]]


#3. *Transposing a Matrix*:

# Create a matrix
matrix = [[1, 2],
          [3, 4],
          [5, 6]]

# Transpose the matrix
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(transpose)  # Output: [[1, 3, 5], [2, 4, 6]]


#4. *Multiplying a Matrix by a Scalar*:

# Create a matrix
matrix = [[1, 2],
          [3, 4]]

# Multiply by scalar 2
result = [[element * 2 for element in row] for row in matrix]

print(result)  # Output: [[2, 4], [6, 8]]


#5. *Checking if an Element Exists in the Matrix*:

# Create a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Check if element 5 exists in the matrix
element = 5
exists = any(element in row for row in matrix)

print(exists)  # Output: True


# HOW TO IMPLEMENT A SWITCH-CASE IN 2D ARRAYS 
def case1():
    print("Sam")

def case2():
    print("Elton")

def case3():
    print("yasin")

switch = {
    1: case1,
    2: case2,
    3: case3
}

#### DONE ####