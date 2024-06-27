import numpy as np 

#creating a 1D array
arr =np.([1,2,3,4,5])
print(arr)

# creating a 2D numpy array(Matrix)
matrix=np.array([[2,3,5],[0,2,4]])# nested python list(a lit with other list within)
print(matrix)
print(matrix.shape)
print(matrix.dtype)
print(matrix.ndim)

# Numpy array attributes(shape & Dinamension)
print(matrix.shape)
print(matrix[:,2])
