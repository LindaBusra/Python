"""
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myjob = "engineer"
my_job = "engineer"
_myjob = "engineer"
MYJOB = "engineer"
myJob = "engineer"
myJob3 = "engineer"

#illegal
#2myjobb = "engineer"
#my-job = "engineer"
#my job = "engineer"

#Assign multiple variables
x, y, z = "Banana", "Orange", "Cherry";
print(x, y, z)

#Asisign one value to multiple variables
x=y=z="Orange"
print(x, y, z)

"""Unpack a Collection
If you have a collection of values in a list,  
Python allows you to extract the values into variables. This is called unpacking."""

fruits = ["apple", "orange", "cherry"]
x,y,z = fruits
print(x, y, z)
print(x)


#Output variables
x = "Python"
y = "is"
z = "perfect"
print(x, y, z)
print(x +  y + z)           #No space between words


#mathematical operator
x = 5
y = 10
print(x+y)

#gives error
z = "Java"
print(x + z)