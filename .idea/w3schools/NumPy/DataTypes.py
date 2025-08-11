# NumPy Data Types

'''
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
'''

# Checking the Data Type of an Array
# The NumPy array object has a property called dtype that returns the data type of the array:

print("Get the data type of an array object:")
import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)        # int64

arr = np.array(["apple", "cherry", "banana"])
print(arr.dtype)        # U6


# Creating Arrays With a Defined Data Type
arr = np.array([1,2,3,4,5], dtype='S')
print(arr.dtype)        # S



# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# A non integer string like 'a' can not be converted to integer (will raise an error):
#arr = np.array(['a', '2', '3'], dtype='i')      # ValueError: invalid literal for int() with base 10: 'a'



# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
print("\nChange data type from float to integer by using 'i' as parameter value:")
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr.dtype)     #int32
print(newarr)           #[1 2 3]


print("\nChange data type from float to integer by using int as parameter value:")
secondarr = arr.astype(int)
print(secondarr.dtype)  #int64
print(secondarr)        #[1 2 3]


print("\nChange data type from integer to boolean:")
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr.dtype)
print(newarr)           #[ True False  True]


print("\nWhat will be the printed result?")
arr = np.array([-1, 0, 1])
newarr = arr.astype(bool)
print(newarr)





'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''