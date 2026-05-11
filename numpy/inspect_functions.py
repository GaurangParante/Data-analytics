import numpy as np

# a = [30,40,20,40,30]
a = [[30,40,40],[20,40,30]]
arr = np.array(a)

print(arr)

print(arr.shape) # Rows, Columns

print(len(arr)) # Number of nested value

print(np.size(arr)) # Number of elements

print(type(arr)) # type of variables

print(arr.dtype) # Datatypes of array

print(arr.astype(float)) # Conversion of datatypes