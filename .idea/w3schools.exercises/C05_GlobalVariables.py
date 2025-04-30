
#If a variable is created outside the function, it is global variable.
#They can be used both inside of functions and outside

x = "It is wonderfull"

def myFunction():
    y="perfect"
    x="fantastisk"
    print("Python is " + x)


myFunction()        #Python is fantastisk
print(x)            #It is wonderfull
#print(y)            #it gives error


 #If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global h
    h = "is perfect"
    print(h)

myfunc()
print("Java " + h)


#we can change global variable inside a function
y = "Java"

def language():
    global y
    y = "Python"
    print(y)

language()
print("My favourite is " + y)