import C41_mymodule

C41_mymodule.greeting("Emily")


a = C41_mymodule.person1["age"]
print(a)
b=C41_mymodule.person1["name"]
print(b)


#Re-naming a Module
#You can create an alias when you import a module, by using the as keyword:

import C41_mymodule as mymodule

a = mymodule.person1["age"]
print(a)


#Built-in Modules
#There are several built-in modules in Python, which you can import whenever you like.

import platform
x = platform.system()
print(x)        #Windows


#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
x = dir(platform)
print(x)

#The dir() function can be used on all modules, also the ones you create yourself.
a =dir(mymodule)
print(a)


#Import only the person1 dictionary from the module:
from C41_mymodule import person1
print (person1["age"])

#When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]


#What is the correct syntax of printing all variables and function names of the "mymodule" module?
import mymodule

print(dir(mymodule))