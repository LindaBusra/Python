
# Open a File on the Server
# The open() function returns a file object, which has a read() method for reading the content of the file:

import os
os.chdir("c:/Users/busra/Desktop/NTNU/InformasjonsTeknologi/Python/w3schools/FileHandling")
print("To open a file for reading it is enough to specify the name of the file:")
f = open("demofile.txt")
print(f.read())


# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

print("\nReturn the 5 first characters of the file:")
f = open("demofile.txt", "r")
print(f.read(5))


# Read Lines
# You can return one line by using the readline() method:
print("\nRead one line of the file:")
f = open("demofile.txt")
print(f.readline())


# By calling readline() two times, you can read the two first lines:
print("\nRead two lines of the file:")
f = open("demofile.txt")
print(f.readline())
print(f.readline())


# By looping through the lines of the file, you can read the whole file, line by line:
print("\nLoop through the file line by line:")
f = open("demofile.txt")
for x in f:
    print(x)
    
    
# Close Files
# It is a good practice to always close the file when you are done with it.    
print("\nClose the file when you are finished with it:")
f = open("demofile.txt", "r")
print(f.read())
f.close


print("-------------------------------------------------")

#read tall.txt
f = open("tall.txt")
content = f.read()
print(content)
f.seek(0) 

matrix = []
total_sum = 0


for line in f:
    num_list = line.split() 
    num_list = [int(element) for element in num_list]  # Her elemanı integer'a çevir
    matrix.append(num_list) 
    total_sum += sum(num_list)  # Satırdaki sayıların toplamını genel toplama ekle

f.close() 

# Toplamı yazdır
print("The total sum: " + str(total_sum))
     



print("------------OR-------------------------")

#read tall.txt
f = open("tall.txt")
content = f.read()
print(content)
f.seek(0) 

matrix = []
total_sum = 0

for line in f:
    num_list = line.split() 
    for x in num_list:
        total_sum += int(x)

f.close() 

# Toplamı yazdır
print("The total sum: " + str(total_sum))


print("------------------last solution--------------------------------------")

matrix = []  
total_sum = 0 

f = open("tall.txt")  
print("Reading file...")  

for line in f:
    num_list = line.split() 
    num_list = [int(x) for x in num_list]    
    matrix.append(num_list) 
    total_sum =+ sum(num_list) 
f.close() 

print("The total sum:" + str(total_sum)) 

     