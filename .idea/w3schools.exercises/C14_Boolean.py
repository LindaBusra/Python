print(10>9)
print(10<9)
print(8==6)

a=200
b=33

if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")




#The bool() function allows you to evaluate any value, and give you True or False in return
""" Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.   """

print(bool("hello"))
print(bool(15))
print(bool("abc"))
print(bool(["apple", "cherry", "banana"]))
print(bool(" "))        #it is not empty, it has space

#The following will return False:
print(bool(""))
print(bool(0))
print(bool(False))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))


def myFunction() :
    return True

print(myFunction())

if myFunction():
    print("Yes")
else:
    print("No")


#isinstance() function used to determine if an object is of a certain data type:
x =600
print(isinstance(x, int))       #True