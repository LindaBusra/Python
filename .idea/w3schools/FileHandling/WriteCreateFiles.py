
'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''
import os
os.chdir("c:/Users/busra/Desktop/NTNU/InformasjonsTeknologi/Python/w3schools/FileHandling")


print("Open the file 'demofile2.txt' and append content to the file:")
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#-----------------------------------------------------------------------------------------------

# The "w" method will overwrite the entire file.
print("\nOpen the file 'demofile3.txt' and overwrite the content:")
f =open("demofile3.txt", "w")
f.write("I have deleted the context!!!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())



'''
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exists
'''

print("\nCreate a file called 'myfile.txt':")
f = open("myfile.txt", "x")     # Result: a new empty file is created!
f = open("myfile.txt", "w")     # Create a new file if it does not exist:
