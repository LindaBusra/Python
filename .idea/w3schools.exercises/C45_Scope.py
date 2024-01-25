# Scope: A variable is only available from inside the region it is created. This is called scope.

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 500
def main_function():
    print(x)

main_function()     #500
print(x)            #500




#Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# Example : The function will print the local x, and then the code will print the global x:
a = 300

def function1():
    a = 200
    print(a)        #200

function1()
print(a)            #300


print("\n--------------------------------------------------------------------------------------")


#Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
# Example : If you use the global keyword, the variable belongs to the global scope:
def function2():
    global x
    x = 300
    y = 500

function2()
print(x)
#print(y)  #it gives error, because it defines just in the function


print("\n--------------------------------------------------------------------------------------")


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)


print("\n--------------------------------------------------------------------------------------")



# A variable created inside a function is available inside that function:
def myFunction():
    y = 300
    print(y)

myFunction()

#the variable x is not available outside the function, but it is available for any function inside the function:
def myFunction():
    a = 300
    def myInnerFunction():
        print(a)
    myInnerFunction()

myFunction()