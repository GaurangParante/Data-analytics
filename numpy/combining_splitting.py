import numpy as np
# a = [30,40,50]
# b = [5,5,3]
# print(a+b)

# Concatenate
# arr1 = np.array([30,40,50])
# arr2 = np.array([5,5,3])

# print(np.concatenate([arr1,arr2]))
# print(np.concatenate([arr1,arr2],axis=0))

# arr1 = np.array([[30,40],[50,10]])
# arr2 = np.array([[5,5],[3,3]])

# print(np.concatenate([arr1,arr2],axis=0))
# print(np.concatenate([arr1,arr2],axis=1))
# print(np.hstack([arr1,arr2])) # Horizontal Concatenation
# print(np.vstack([arr1,arr2])) # Vertical Concatenation

# a = np.array([20,40,30,40,10,20])
# print(np.array_split(a,3))
a = np.array([[20,40,30],[40,10,20]])
b = np.array_split(a,2)
print(b)
print(b[1])