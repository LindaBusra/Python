
# NumPy Array Copy vs View

# COPY  : Make a copy, change the original array, and display both arrays:
print("Make a copy, change the original array, and display both arrays:")
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
x[0] = 42
print(arr)      # [1 2 3 4 5]
print(x)        # [42  2  3  4  5]


# VIEW:The view SHOULD be affected by the changes made to the original array.
print("\nMake a view, change the original array, and display both arrays:")
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 55
print(arr)      # [55  2  3  4  5]
print(x)        # [55  2  3  4  5]


print("\nMake a view, change the view, and display both arrays:")
arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 65
print(arr)      # [65  2  3  4  5]
print(x)        # [65  2  3  4  5]


# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.


print("\nPrint the value of the base attribute to check if an array owns it's data or not:")
arr = np.array([1,2,3,4,5])
x= arr.copy()
y= arr.view()

print(x.base)   #None
print(y.base)   #[1 2 3 4 5]

#The copy returns None.
#The view returns the original array.