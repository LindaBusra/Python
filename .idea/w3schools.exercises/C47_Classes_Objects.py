# Create a Class
# To create a class, use the keyword class:
class MyClass:
    x = 5


# we can use the class named MyClass to create objects:
p1 = MyClass()
print(p1.x)


#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 25)
print(p1.name)
print(p1.age)


print("\n--------------------------------------------------------------------------------------")


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1)       #<__main__.Person object at 0x0000019A36FD16D0>



print("\n--------------------------------------------------------------------------------------")



#Example
# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name:{self.name}, age:{self.age}"

p1 = Person("John", 36)
print(p1)


print("\n--------------------------------------------------------------------------------------")


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Example : Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("My name is: " + self.name)

p1 = Person("John", 33)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


print("\n--------------------------------------------------------------------------------------")


# Use the words myObject and abc instead of self:
class Person:
    def __init__(myObject, name, age):
        myObject.name = name
        myObject.age = age

    def myfunction(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Emily", 30)
p1.myfunction()


print("\n--------------------------------------------------------------------------------------")


# You can modify properties on objects like this, Set the age of p1 to 40:
p1.age = 40


#Delete the age property from the p1 object:
del p1.age


#You can delete objects by using the del keyword:
del p1



#class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.
class Person:
    pass


