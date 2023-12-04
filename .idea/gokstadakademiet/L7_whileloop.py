#Lesson 04_09_2023


#while loops
alder = 0

while alder<18:
    print("Du er fortsatt bare: " +  str(alder))
    alder +=1



#Still spørsmål til du får svar:
svar = ""

while svar == "":
    svar = input("Gi meg et svar")


#break - continiue
navnListe =  ["Mike", "Emily", "Yngve", "Petter", "Per", "Kristin"]

#continue
for navn in navnListe:
    if navn == "Yngve":
        continue
    print(navn)


#break
for navn in navnListe:
    if navn == "Petter":
        break
    print(navn)




#infinitive loop
# while True:
#     print("Python")



