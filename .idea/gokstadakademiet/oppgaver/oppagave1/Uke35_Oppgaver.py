#Oppgave 1: Variabler og Datatyper
#Lag en variabel kalt alder og tildel den din egen alder. Skriv deretter ut alderen ved hjelp av print().
alder =47
print("Min alder er: ", alder)


#Oppgave 2: Input og Datatyper
#Be brukeren om å oppgi navnet sitt ved hjelp av input(). Lagre dette i en variabel og skriv
#deretter ut en hilsen som inkluderer navnet. F.eks Hei navn!
navn = input("Vennligst skriv inn ditt navn: ")
print("Hei", navn.title())  #hvis man skriver navn som oLE, ved hjelp av title kan vi redigere det sånn : Ole


#Oppgave 3: Aritme7ske Operatorer
#Be brukeren om to tall, et heltall og et desimaltall. Utfør addisjon, subtraksjon, multiplikasjon
#og divisjon av tallene og skriv ut resultatet.
heltall = int(input("Vennligst skriv inn et heltall: "))
desimaltall = float(input("Vennligst skriv inn et desimaltall: "))
print("Addisjon for", heltall, "og", desimaltall, "er", (heltall+desimaltall))
print("Subtraksjon for", heltall, "og", desimaltall, "er", (heltall-desimaltall))
print("Multiplikasjon for", heltall, "og", desimaltall, "er", (heltall*desimaltall))
print("Divisjon for", heltall, "og", desimaltall, "er", (heltall/desimaltall))


#Oppgave 4: Sammenligningsoperatorer
#Be brukeren om to tall og sammenlign dem ved å skrive ut om det første tallet er større enn,
#mindre enn eller lik det andre tallet.
tall1 = int(input("Vennligst skriv inn det første tallet: "))
tall2 = int(input("Vennligst skriv inn det andre tallet: "))

if tall1>tall2:
    print(tall1, "er større enn", tall2)
else:
    print(tall1, "er mindre enn eller lik", tall2)


"""Oppgave 5: UJorsk Logiske Operasjoner med Boolske Verdier
I denne oppgaven vil vi utforske logiske operasjoner (AND, OR, NOT) med boolske verdier.
Følg instruksjonene nedenfor:
- Be brukeren om to boolske verdier (True eller False).
- Konverter inndataene til boolske verdier ved å sammenligne dem med strengen
"true" (ignorerer store/små bokstaver).
- UJør følgende logiske operasjoner:
o AND-operasjon: Resultatet er True hvis begge verdiene er True, ellers False.
o OR-operasjon: Resultatet er True hvis minst én av verdiene er True, ellers
False.
o NOT-operasjon: Resultatet er den motsatte verdien av den opprinnelige
verdien.
- Skriv ut resultatet av hver operasjon."""

boolean1= bool(input("Du er voksen. For svar velg en av dem: True-False: ").title()=="True")
boolean2 = bool(input("Du bor i Haugesund. For svar velg en av dem: True-False: ").title()=="True")

print("AND-operasjon:", boolean1 and boolean2)
print("OR-operasjon:", boolean1 or boolean2)
print("NOT-operasjon:", not(boolean1) )
print("NOT-operasjon:", not(boolean2) )



#Oppgave 6: Typekonvertering
#Be brukeren om en temperatur i Celsius. Konverter denne 7l Fahrenheit og skriv ut
#resultatet.
celsius = float(input("Vennligst skriv inn temperaturen i Celsius: "))
fahrenheit = 32 + (celsius * 9/5)
print("Temperaturen i Fahrenheit er: ", fahrenheit)


#Oppgave 7: Beregninger med Tekst
#Be brukeren om navn og alder. Lag en setning som kombinerer navn og alder, for eksempel
#    "Hei, Per! Du er 20 år gammel."
navn=input("Kan du skrive ditt navn?")
alder=int(input("Kan du skrive din alder?"))
print("Hei", navn.title(), "\b! Du er", alder, "år gammel.")


#Oppgave 8: Typekonvertering
#Be brukeren om en desimalverdi. Konverter den till et heltall og skriv ut resultatet.
decimaltall = float(input("Kan du skrive et decimall tall: "))
heltall = int(decimaltall)
print("Etter konvert tallet er:", heltall)


#Oppgave 9: Aritmetiske Operatorer
#Be brukeren om et tall og skriv ut kvadratet og kubikken av tallet.
tall = int(input("Kan du skrive et tall: "))
print("Kvadratet av tallet: ", tall**2)
print("Kubikken av tallet: ", tall**3)


#Oppgave 10: Strenger og Operatorer
#Be brukeren om sitt favorittord. Skriv ut ordet tre ganger, hver gang med mellomrom og uten mellomrom.
favorittord = input("Hva er ditt favorittord: ")
print(favorittord, favorittord, favorittord)
print(favorittord + favorittord + favorittord)


#Oppgave 11: Sammenligningsoperatorer
#Be brukeren om to tall og skriv ut True hvis differansen mellom tallene er mindre enn 10,
#ellers skriv ut False.
tall1 = int(input("Vennligst skriv inn det første tallet: "))
tall2 = int(input("Vennligst skriv inn det andre tallet: "))
differanse = abs(tall1-tall2)

if differanse<10:
    print("True")

else:
    print("False")



#Oppgave 12: Regn ut Arealet av en Rektangel
#Be brukeren om å oppgi lengden og bredden til en rektangel. Regn deretter ut arealet av
#rektangelet og skriv det ut.
lengd = float(input("Hva er lengden til rektangel?: "))
bred = float(input("Hva er bredden til rektangel?: "))

print("Arealet av Rektangel: ", lengd*bred)