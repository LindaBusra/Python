# File Handling
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


#To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")    #same as f = open("demofile.txt", "rt")  r for read, t for text are the default values

#read() method for reading the content of the file:
print(f.read())


print("\n----------------------------------------------------------------------------------")


#If the file is located in a different location, you will have to specify the file path, like this:
f= open("C:\\Users\\busra\\IdeaProjects\\Python\\.idea\\exercises\\text.txt")
print(f.read())


print("\n----------------------------------------------------------------------------------")

#Read Only Parts of the File
#read() method returns the whole text, but you can also specify how many characters you want to return:

#Example - Return the 6 first characters of the file:
f = open("demofile.txt")
print(f.read(6))


print("\n----------------------------------------------------------------------------------")

#Read Lines
#You can return one line by using the readline() method:
f = open("demofile.txt")
print(f.readline())     #Read one line of the file:

print("\n----------------------------------------------------------------------------------")

#By calling readline() two times, you can read the two first lines:
f = open("demofile.txt")
print(f.readline())     #Read one line of the file:
print(f.readline())     #Read one line of the file:


print("\n----------------------------------------------------------------------------------")

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt")
for x in f:
    print(x)

print("\n----------------------------------------------------------------------------------")


#Close Files : It is a good practice to always close the file when you are done with it
f = open("demofile.txt")
print(f.readline())
f.close()