#Creating a Function
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#Information can be passed into functions as arguments.

def myFunction():
    print("I am a function")

myFunction()



#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.
def names(fname):       #fname-->parameter
    print("Welcome", fname)

names("Emily")      #Emily-->argument
names("Mike")


def full_name(name, lastname):
    print("You are: ", name, lastname)

full_name("Emily", "Nilsen")
full_name("Mike", "Johnson")


#Arbitrary Arguments, *args
#If the number of arguments is unknown, add a * before the parameter name:
def my_kids(*kids):
    print("the youngest child is " + kids[2])

my_kids("Emil", "Tobias", "Jane", "Mike")


#Keyword Arguments
#You can also send arguments with the key = value syntax. With this way order is not matter
def my_kids(kid1, kid2, kid3):
    print(kid2)

my_kids(kid3="Emily", kid2="Tom", kid1="Jake")    #it prints Tom


#Arbitrary Keyword Arguments, **kwargs
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_family(**kid):
    print("His last name is " + kid["lastname"])

my_family(fname="Tobisas", lastname="Nilsen")



#Default Parameter Value
#If we call the function without argument, it uses the default value:
def countries(country="Norway"):
    print("I am from " + country)

countries("India")
countries("USA")
countries()             #default-->I am from Norway
countries("Canada")



#Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "cherry", "banana"]
my_function(fruits)



#Return Values
#To let a function return a value, use the return statement:
def new_function(x):
    return 5*x

print(new_function(4))



#The pass Statement
#function definitions cannot be empty, but if you for some reason have a function definition
# with no content, put in the pass statement to avoid getting an error.
def myfunction():
    pass


#Recursion : a defined function can call itself.
def try_recursion(k):
    if(k > 0):
        result = k + try_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
try_recursion(6)