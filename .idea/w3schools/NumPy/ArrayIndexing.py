
# NumPy Array Indexing
# Access Array Elements
# You can access an array element by referring to its index number.

print("Get the first element from the following array:")
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[0])


print("\nGet third and fourth elements from the following array and add them.")
print(arr[2] + arr[3])


# Access 2-D Arrays
print("\nAccess the element on the first row, second column:")
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0][1])
#or
print('2nd element on 1st row: ', arr[0, 1])


print("\nAccess the element on the 2nd row, 5th column:")
print('5th element on 2nd row: ', arr[1, 4])


# Access 3-D Arrays
print("\nAccess the third element of the second array of the first array:")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0,1,2])



# Negative Indexing
print("\nPrint the last element from the 2nd dim:")
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[1, -1])


# Exercise
print("\nWhat will be the printed result?")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])