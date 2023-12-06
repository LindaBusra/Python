#Undervisning 4 - 11.09.2023

#Definering og kall av funksjoner
#Funksjoner er kodeblokker som utfører en bestemt oppgave når de blir kalt.

def si_hei():
    print("Hei, verden!")

#kall funksjonen
si_hei()




#Return statements brukes i funksjoner for å sende tilbake resultater til kallet.
def multipliserer(a,b):
    resultat = a*b
    return resultat

#kall funskonen og lagre resultatet i en variabel
produkt = multipliserer(4, 5)
print(f"Produktet er: {produkt}")




#Parametere og argumenter
#Parametere er variabler som funksjoner tar imot
#Argumenter er de faktiske verdiene som sendes inn i funksjonen.
def hilsen(navnet):
    print(f"Hei, {navnet}")

#Kall funksjonen med et argument
hilsen("Emily")



#Scope av Variabler
#Scope refererer til gyldighetsområdet til en variabel
def funksjon1():
    lokal_variabel=10
    print(f"Inne i funksjonen1: {lokal_variabel}")

#Kall funksjonen
funksjon1()


global_variabel = 20

def funksjon2():
    print(f"Inne i funksjonen2: {global_variabel}")

#Kall funksjonen
funksjon2()

print(f"Utenfor funksjon2:  {global_variabel}")





#Bruk av import
#Import står for å hente eksterne moduler og biblioteker i Python
import math

#Bruk av funksjoner fra math-modulen
kvadratrot = math.sqrt(25)
print(f"Kvadratrot av 25 er: {kvadratrot}")



#Introduksjon til Random Modulen
#Random modulen gir funksjoner for generering av tilfeldige tall og valg
import random

tilfeldig_tall = random.randint(1,10)
print(f"Tilfeldig tall: {tilfeldig_tall}")


farger = ["rød", "grønn", "blå", "gul"]
tilfeldig_farge = random.choice(farger)
print(f"Tilfeldig valgt farge: {tilfeldig_farge}")




#Practice-1
def si_hei():
    print("Hei folkens!")

si_hei()


#Practice-2, funksjon with parameter
def hilsen(navn):
    print(f"Hei {navn}")

hilsen("Emily Nilsen")



#Practice-3, funksjon som returnerer en verdi


def summer(a, b):
    resultat = a+b
    return resultat

total_sum = summer(33,37)
print("Total summen er: ", total_sum)





#samme spørsmål with global variabel

sum = 0 #global variabel

def summer(a, b):
    sum = a+b
    return sum

total_sum = summer(33,37)
print("Total summen er: ", total_sum)



#Practice-4, funksjon som returnerer en verdi
def multipliser(a,b):
    resultat = a*b
    return resultat

sum = multipliser(4, 3)
print(f"Produktet av tallene er: {sum}")




#Practice-5, funksjon som returnerer enkvadrat liste
def kvadratliste(tall):
    kvadrater = []
    for i in range(1, tall+1):  #range(a, b)-->(inclusive, exclusive)
        kvadrater.append(i ** 2)        #i^2
    return kvadrater


inputTall = int(input("Skriv in ett tall: "))
resultatListe = kvadratliste(inputTall)
print(f"Kvadrater av tallene: {resultatListe}")



#Practice-6
def legg_sammen(a, b):
    resultat = a+b
    print(f"Summen av {a} og {b} er {resultat}")

legg_sammen(7,12)



#Practice-7
def legg_sammen_return(a, b):
    resultat = a+b
    return resultat

res = legg_sammen_return(7,12)
print("Resultatet hentet via return: ", res)