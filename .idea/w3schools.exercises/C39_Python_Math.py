#Math Functions
#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(2,7,9)
y = max(12,45,3)
print(x)
print(y)


#The abs() function returns the absolute (positive) value of the specified number:
x = -65
print(abs(x))
y = abs(-8.56)
print(y)


#The pow(x, y) function returns the value of x to the power of y (x^y).
x = pow(4,3)
print(x)


#The Math Module, Python has also a built-in module called math, which extends the list of mathematical functions.
#To use it, you must import the math module:

import math

x = math.sqrt(64)
print(x)


#The math.ceil() method rounds a number upwards to its nearest integer,
#The math.floor() method rounds a number downwards to its nearest integer, and returns the result:

x =  math.ceil(1.4)
print(x)            #2
y = math.floor(1.4)
print(y)            #1


#The math.pi constant, returns the value of PI (3.14...):
x = math.pi
print(x)