
# Built-in Math Functions

# The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)

# The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4,3)
print(x)        # 64


# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

import math
x = math.sqrt(64)
print(x)        # 8.0


# The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x = math.ceil(4.6)
y = math.floor(4.6)
print(x)        # 5
print(y)        # 4


# The math.pi constant, returns the value of PI (3.14...):
print(math.pi)      # 3.141592653589793

