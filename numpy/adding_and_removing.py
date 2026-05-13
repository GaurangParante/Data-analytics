import numpy as np

# a = np.array([20,40,60,80]) # 1D array
a = np.array([[20,40],[60,80]]) # 2D array

# Append Method


# print(np.append(a,90))

# print(np.append(a,90))

# print(np.append(a,[90,100]))


# Insert Method


# print(np.insert(a,3,50)) # np.insert(array_name,index,value) for 1D example

# print(np.insert(a,3,50)) # np.insert(array_name,index,value) for 2D example

# print(np.insert(a,1,[50,60],axis=1)) # np.insert(array_name,index,[value],axis) for 2D example

# print(np.insert(a,1,[50,60],axis=0)) # np.insert(array_name,index,[value],axis) for 2D example

# print(np.insert(a,1,[50],axis=0)) # np.insert(array_name,index,[value],axis) for 2D example single value is like [50,50]

# print(np.insert(a,[0,2],[50],axis=0)) # np.insert(array_name,index,[value],axis) for 2D example for multiple index


# Delete method

# print(np.delete(a,1)) # its remove single data Due to convert array in 1D and then remove from tha index
print(np.delete(a,1,axis=1)) # Its remove by axis data
