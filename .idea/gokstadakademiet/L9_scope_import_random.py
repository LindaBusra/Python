#Bruk av nøkkelargumenter
def hilsen(navn, alder):
    print(f"Hei, {navn}! Du er {alder} år gammel")

hilsen("Ole", 34)

#or
def hilsen(navn, alder):
    print(f"Hei, {navn}! Du er {alder} år gammel")

hilsen(alder=45, navn="Ola")



def funksjon1():
    lokal_variable= 10      #den er tilgjengelig kun inni funksjonen
    print(f"Inne i funksjon1: {lokal_variable}")

funksjon1()

#her nede vi får error fordi lokal_variable er tilgjengelig kun inni funksjonen
#print(f"Utenfor funksjonen1: {lokal_variable}")




global_variabel = 20

def funksjon2():
    print(f"Inne i funksjon2: {global_variabel}")

funksjon2()

print(f"Utenfor funksjon2: {global_variabel}")



#import modulen
import math     #mathematikk module

kvadratrot = math.sqrt(25)
print(f"Kvatratroten av 25 er: {kvadratrot}")



#bruk av randint fra random modulen
from random import randint

tilfeldig_tall = randint(1,100)
print(f"Tilfeldig tall: {tilfeldig_tall}")


#import hele random modulen
import random
tilfeldig_tall = random.randint(1,100)
print(f"Tilfeldig tall: {tilfeldig_tall}")



#practice-1
farger = ["rød", "grønn", "blå", "hvit", "gul"]
tilfeldig_farge = random.choice(farger)
print(f"Tilfeldige valgt farge: {tilfeldig_farge}")


#blande liste tilfeldig
kortstokk = ["Hjerter", "ruter", "spar", "klover"]
random.shuffle(kortstokk)       #blander elementer
print("Blandet kortstokk: " , kortstokk)









