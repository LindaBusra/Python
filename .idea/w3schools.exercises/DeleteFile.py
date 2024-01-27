#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function:
import os


#Check if File exist:
if os.path.exists("demofile_forDelete.txt"):
    os.remove("demofile_forDelete.txt")
else:
    print("The file does not exist")


#Remove the file "demofile.txt":
# os.remove("demofile.txt")


#Delete Folder:  To delete an entire folder, use the os.rmdir() method:
os.rmdir("forDelete")           #Note: You can only remove empty folders.