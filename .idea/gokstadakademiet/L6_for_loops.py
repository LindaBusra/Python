#Lesson 04_09_2023

#for loops


for i in range(0,10):
    print(i)



for i in range(0,10):       #print in samme linje
    print(i, end ="")


print("-----------------------------------------------------------------------")


fruktliste = ["eple", "banan","appelsin"]
print(len(fruktliste))


#print the items in list
for i in range(0,len(fruktliste)):
    print(fruktliste[i])


#print the items in list
for frukt in fruktliste:
    print(frukt)


#contains
for frukt in fruktliste:
    if "e" in frukt:
        print("Frukten: " + frukt +  " inneholder bokstaven e")




