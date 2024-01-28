#Oppgave 13: Aritmetiske Operatorer
#Be brukeren om et starttall og et tall som representerer en økning. Lag en løkke som skriver
#ut de første 10 tallene i en aritmetisk rekke med dette starttallet og økningen.

starttall = int(input("Vennligst skriv inn et starttall: "))
økning_tall = int(input("Vennligst skriv inn et tall som representerer en økning: "))

for i in range(10):     #i=0,1,2,...,9
    ny_tall = starttall + i * økning_tall
    print(ny_tall)




#Oppgave 14: Betingelser og Løkker
#Lag en løkke som skriver ut alle partall fra 10 til 30, men ikke tall som er delelige med 6.

for i in range(10,31):
    if (i%6!=0):
        print(i)



#Oppgave 15: Datatyper og Typekonvertering
#Be brukeren om et ord og skriv ut hvert bokstav i ordet som en egen streng.
ord = input("Vennligst skriv inn et ord: ")

for i in ord:
    print(i)



#Oppgave 16: Sammenligningsoperatorer
#Be brukeren om tre tall. Skriv ut True hvis de tre tallene er i stigende rekkefølge, ellers skriv
#ut False.

tall1 = int(input("Vennligst skriv inn tall 1: "))
tall2 = int(input("Vennligst skriv inn tall 2: "))
tall3 = int(input("Vennligst skriv inn tall 3: "))

if (tall1<tall2 and tall2<tall3):
    print("True")
else:
    print("False")



#Oppgave 17: Løkker og Sammenligninger
#Bruk en løkke til å skrive ut partallene fra 2 til 20.

for i in range(2, 21):
    if i%2==0:
        print(i)



#Oppgave 18: Tekstmanipulasjon
#Be brukeren om en setning. Skriv ut den samme setningen, men med alle bokstavene i store
#bokstaver.
setning = input("Vennligst skriv inn en setning: ")
print(setning.upper())



#Oppgave 19: Avansert: Delbare Tall
#Be brukeren om et heltall. Skriv ut alle tall fra 1 til det oppgitte tallet som er delbare med
#både 3 og 5.
helttall = int(input("Vennligst skriv inn et helttall: "))

for i in range(1, helttall):
    if (i%3==0 and i%5==0):
        print(i)