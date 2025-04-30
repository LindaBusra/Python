#Arbeidskrav 1•Innlevering: Uke 37, fredag 15.september 2023•

#Oppgave 2
#1.Opprett og skriv ut en liste med 5 tilfeldig heltall mellom 1 og 100
import random

list=[]

for i in range(0,5):
    list.append(random.randint(1,100))

print("En liste med 5 tilfeldig heltall: ", list)




#2.Sorter og skriv ut den samme listen med tallene i stigende rekkefølge
list.sort()
print("Listen med tallene i stigende rekkefølge:", list)




#3.Opprett og skriv ut en liste med 100 tilfeldige heltall mellom 1 og 200
list=[]

for i in range(0,100):
    list.append(random.randint(1,200))

print("En liste med 100 tilfeldige heltall: ", list)




#4.I listen med 100 tilfeldig tall skal du nå fjerne alle tall som er større en 100
my_list = []

for i in list:
    if i < 100:
        my_list.append(i)

print("Tallene  som er større en 100 fjernet fra den listen: ", my_list)





#5.I listen med tilfeldigtall skal du nå også fjerne alle tall som er delelig med tre, altså tall som er i 3 gangeren.
new_list = []
for i in my_list:
    if i%3!=0:
        new_list.append(i)

print("Også alle tall som er delelig med tre fjernet i den listen:", new_list)