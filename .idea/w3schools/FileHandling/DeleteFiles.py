import os
os.chdir("c:/Users/busra/Desktop/NTNU/InformasjonsTeknologi/Python/w3schools/FileHandling")

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

os.remove("myfile.txt")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")    
    
    
# Delete Folder
# To delete an entire folder, use the os.rmdir() method:   
# Note: You can only remove empty folders.!!! 
print("\nRemove the folder "myfolder":")
os.rmdir("myfolder")
    
    
    