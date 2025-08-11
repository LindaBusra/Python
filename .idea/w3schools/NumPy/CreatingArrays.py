
# NumPy Creating Arrays

# We can create a NumPy ndarray object by using the array() function.

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))        # <class 'numpy.ndarray'>


# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray:
arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))


'''
Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).
nested array: are arrays that have arrays as their elements.
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array. These are the most common and basic arrays.
An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors.
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
'''

print("\nCreate a 0-D array with value 42")
arr0 = np.array(42)
print(arr0)


print("\nCreate a 1-D array containing the values 1,2,3,4,5")
arr1 = np.array([1,2,3,4,5])
print(arr1)


print("\nCreate a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:")
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)


print("\nCreate a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:")
arr3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr3)


# Check Number of Dimensions?
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print("\nCheck how many dimensions the arrays have:")
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
