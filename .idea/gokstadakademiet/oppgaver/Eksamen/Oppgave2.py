#Oppgave 2 (15%)


#A. Lag en liste som inneholder fem valgfrie frukter.
fruktList = ["Eple", "Banan", "Mango", "Melon", "Kiwi"]


#A.1. Skriv ut alle elementene ved hjelp av en for-løkke.
print("Oppgave 2- A.1")

for x in fruktList:             #å bruke for-each loop
    print(x)
print()




#A.2. Skriv ut alle elementene ved hjelp av en while-løkke.
print("Oppgave 2- A.2")

i = 0

while i<len(fruktList):         #mens i er mindre enn  fruktlist length, den condition is true
    print(fruktList[i])
    i+=1
print()



#B - For hver frukt, tilordne en farge til frukten og opprett en annen liste med disse fargene. Skriv
#ut fruktens navn sammen med dens farge. Eks: "Eplet er rødt."
print("Oppgave 2- B")

fargeList = ["rødt", "gult", "oransje", "grønt", "brunt"]

for i in range(0, len(fruktList)):
    print(f"{fruktList[i]} er {fargeList[i]}.")
print()




#C - Skriv ut det andre og fjerde elementet fra fruktlisten.
print("Oppgave 2- C")

print("Andre frukt i listen: ", fruktList[1])       #for andre elemnt index no=1
print("Fjerde frukt i listen: ", fruktList[3])      #for fjerde elemnt index no=3
print()




#D - Skriv ut fruktlisten i alfabetisk rekkefølge.
print("Oppgave 2- D")

print("Fruktlisten i alfabetisk rekkefølge: ")
fruktList.sort()                #sort() method sorterer liste med alfabetisk rekkefølge
for frukt in fruktList:
    print(frukt)
print()




#E - Lag en dictonary med fruktene som nøkler og deres farger som verdier. Skriv ut hverkombinasjon som "Eple: Rød"
print("Oppgave 2- E")

fruktFargeDictionary = {fruktList[i]: fargeList[i] for i in range(len(fruktList))}      #key kommer fra FruktList, value fra fargeList
print(fruktFargeDictionary)
print()




#F - Du har blitt gitt en liste med dictionaries som inneholder personers navn og alder. Listen er sånn:
list_dicts = [ {"name":"Vegard", "age":50}, {"name":"Tor", "age":22}, {"name":"Siv", "age":30},
               {"name":"Anne", "age":30}, {"name":"Beate", "age":66} ]


#F.1. Sorter listen basert på alder i stigende rekkefølge.
print("Oppgave 2- F.1")

list_dicts.sort(key=lambda x: x['age'])         #sorterer basert på age med stigende rekkefølge, ascending order
for person in list_dicts:
    print(f"Navn: {person['name']}, Alder: {person['age']}")
print()



#F.2. I tilfeller hvor to personer har samme alder, skal du sortere dem alfabetisk basert på navnet.
print("Oppgave 2- F.2")

list_dicts.sort(key=lambda x: (x['age'], x['name']))        #sorterer med age med stigende rekkefølge, samtidig med name med alfabetical order
for person in list_dicts:
    print(f"Navn: {person['name']}, Alder: {person['age']}")