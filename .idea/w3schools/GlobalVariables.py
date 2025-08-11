
# Global variables
x = "awasome"

def myfunc():
    print("Python is", x)
    
myfunc()    


# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function
y = "awesome"

def about():
    y = "fantastic"
    print("Python is", y)
    
about()                 #Python is fantastic
print("Python is", x)   #Python is awasome


def myfunc():
    global m
    m = 'fantastic'
    
myfunc()    
print("Homework is", m)    




# use the global keyword if you want to change a global variable inside a function.

a = 'best'

def myfunc():
    global a
    a = 'worst'
    
myfunc()
print("Los Angeles is", a)    
