# NumPy Array Slicing

'''
Slicing arrays
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
'''

print("Slice elements from index 1 to index 5 from the following array:")
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])      # Note: The result includes the start index, but excludes the end index.


print("\nSlice elements from index 4 to the end of the array:")
print(arr[4:])


print("\nSlice elements from the beginning to index 4 (not included):")
print(arr[:4])


# Negative Slicing
# Use the minus operator to refer to an index from the end:

print("\nSlice from the index 3 from the end to index 1 from the end:")
print(arr[-3:-1])


# STEP
# Use the step value to determine the step of the slicing:
    
print("\nReturn every other element from index 1 to index 5:")    
print(arr[1:5:2])

print("\nReturn every other element from the entire array:")
print(arr[::2])



# Slicing 2-D Arrays
print("\nFrom the second element, slice elements from index 1 to index 4 (not included):")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])


print("\nFrom both elements, return index 2:")
print(arr[0:2, 2])


print("\nFrom both elements, slice index 1 to index 4 (not included), this will return a 2-D array:")
print(arr[0:2, 1:4])


# examples
print("\nWhat will be the printed result?")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:2])


# Insert the correct slicing syntax to print the following selection of the array:
# Everything from (including) the second item to (not including) the fifth item.
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[1:4])


print("\nEvery other item from (including) the second item to (not including) the fifth item.")
print(arr[1:4:2])


print("\nEvery other item from the entire array.")
print(arr[::2])