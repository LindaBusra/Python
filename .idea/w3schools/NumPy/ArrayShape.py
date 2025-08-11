
#NumPy Array Shape

'''
Shape of an Array
The shape of an array is the number of elements in each dimension.
Get the Shape of an Array
NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
'''

print("Print the shape of a 2-D array:")
import numpy as np
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape)        #(2, 4)
#The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.



print("\nCreate an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:")
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print("shape of array: " ,  arr.shape)      #  (1, 1, 1, 1, 4)



print("\nWhat will be the printed result?")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)