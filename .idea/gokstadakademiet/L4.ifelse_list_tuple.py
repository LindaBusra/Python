#Lesson 04_09_2023
#if_else, list, tuple


#se på alderen, og print man er voksen eller ikke
alder = 36

if  alder>= 18:
    print("Denne personen er myndig")
else:
    print("Denne personen er ikke myndig")



#poeng ve resultat
poengsum =12

if poengsum>=90:
    karakter="A"
elif poengsum>=80:
    karakter="B"
elif poengsum>=70:
    karakter="D"
elif poengsum>=60:
    karakter="D"
else:
    karakter="F"

print("Din karakter er: " + karakter)




#spør brukeren kjønn og alder
kjønn="Dame"
alder=18

if not(kjønn == "Mann"):
    print("Dette er ikke en mann")
if alder !=17:
    print("Dette er ikke en voksen")



# in - not in
tekst ="ffbgkssdffbgkssdffbgkssdffbgkssd"

if "f" in tekst:
    print("Teksten inneholder bokstav 'f'")
if "a" not in tekst:
    print("Teksten inneholder ikke bokstav 'a'")




#sjekk to condition with "and" og "or"
name = "Emily"
alder =38

if (name == "Emily" and alder!=30):   # or  (name == "Emily" or alder==30)
    print("Det stemmer")
else:
    print("Det stemmer ikke")




print("------------------------------------------------------------")

fruktliste= []      #empty list
print(fruktliste)
fruktliste = ["eple", "banan","appelsin"]
print(fruktliste)
grønnsak = ["gulrot", "brokkoli","tomat"]

handleliste = fruktliste + grønnsak     #samle to list
print(handleliste)

fruktliste.extend(grønnsak)     #add second list to first list
print(fruktliste)

handleliste.append("salat")     #add an item in alist
print(handleliste)

handleliste.pop()       #pop() removes the last item
print(handleliste)

print(handleliste[1])       #gives the item which has index no 1
print(handleliste[-1])      #gives the last item

handleliste.remove("tomat") #remove element which name is "tomat"
print(handleliste)



print(fruktliste)
del(fruktliste[1])      #gives the item which has index no 1
print(fruktliste)
del(fruktliste[0:2])    #gives the items which has index no 0,1  (2 is not inclusive)
print(fruktliste)

print("----------------------------------------------------------------------")

fruktliste = ["eple", "banan","appelsin"]
grønnsak = ["gulrot", "brokkoli","tomat"]

handleliste = fruktliste + grønnsak
print(handleliste)

#slicing
print(handleliste[:3])  #print items with index no 0,1,2
print(handleliste[-3:])  #print last 3 items
print(handleliste[1:4])  #print a part of list
print(handleliste[1:-1])  #print a part of list


print("----------------------------------------------------------------------")


#numbers are not changeable in tuple
tuple = (5, 10, 6)
x, y, z = tuple
print("x-koordinat:", x)
print("y-koordinat:", y)
print("y-koordinat:", z)


print(2, tuple, 9)      # 2 (5, 10, 6) 9

x=3
print(2, tuple, 9)  #x endret ikke

print(tuple[0])
print(tuple.count())      # number of element = 5





















