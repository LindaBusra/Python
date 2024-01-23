#Python Try Except
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

#Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

try:
    print(x)
except:
    print("An exception occurred")


#Example : This statement will raise an error, because x is not defined:
#print(x)
print("\n--------------------------------------------------------------")

#Many Exceptions
#Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
print("\n--------------------------------------------------------------")

#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")      #In this example, the try block does not generate any error:
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")     #this line prints

print("\n--------------------------------------------------------------")

try:
    print(y)      #In this example, the try block generate any error:
except:
    print("Something went wrong")   #this line prints
else:
    print("Nothing went wrong")


#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
print("\n--------------------------------------------------------------")
try:
    print("x")                              #this line prints
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")             #this line prints
finally:
    print("The 'try except' is finished")   #this line prints

#or
print("\n--------------------------------------------------------------")

try:
    print(x)
except:
    print("Something went wrong")           #this line prints
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")   #this line prints



#This can be useful to close objects and clean up resources:
#Example: Try to open and write to a file that is not writable:
print("\n--------------------------------------------------------------")
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum ipsum")
    except:
        print("Something went wrong when writing to the file")  #I have this file.
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")



#To throw (or raise) an exception, use the raise keyword.
#Example - Raise an error and stop the program if x is lower than 0:
x = -2

if x < 0:
    raise Exception("Sorry, no numbers below zero")


#Example - Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")