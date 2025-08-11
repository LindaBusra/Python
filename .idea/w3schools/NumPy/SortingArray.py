
# NumPy Sorting Arrays

import numpy as np

print("Sort the array")
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))     # [0 1 2 3]     Note: This method returns a copy of the array, leaving the original array unchanged.


print("\nSort the array alphabetically:")
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))     # ['apple' 'banana' 'cherry']


print("\nSort a boolean array:")
arr = np.array([True, False, True])
print(np.sort(arr))     # [False  True  True]


# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:
print("/nSort a 2-D array:")
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
