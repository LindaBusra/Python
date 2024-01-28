f = open("demofile_forOverwrite.txt", "w")
f.write("I changed the content!!!")
f.close()

#open the file after the overwriting:
f = open("demofile_forOverwrite.txt")
print(f.read())

#Note: the "w" method will overwrite the entire file.