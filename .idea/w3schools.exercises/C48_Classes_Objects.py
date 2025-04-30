#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object and then execute the printname method:
x = Person("Emily", "Nilsen")
x.printname()


#Create child class-->send the parent class as a parameter when creating a child class
class Student(Person):
    pass

#pass:Use the pass keyword when you do not want to add any other properties or methods to the class.
#Now the Student class has the same properties and methods as the Person class

x = Student("Mike", "Jackson")
x.printname()


#We want to add the __init__() function to the child class (instead of the pass keyword).
#When you add the __init__() function, the c    hild class will no longer inherit the parent's __init__() function.

# class Student(Person):
#     def __init__(selfself, fname,lname):


#The child's __init__() function overrides the inheritance of the parent's __init__() function.
