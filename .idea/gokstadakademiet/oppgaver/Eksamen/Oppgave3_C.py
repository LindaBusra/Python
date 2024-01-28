#Oppgave - 3


#3.C -  Skriv en funksjon som tar en radius som inndata og returnerer arealet av en sirkel med den
#radiusen. (Tips: import math -> og bruk math.pi). Den bør også sjekke at inndataen er positiv
#og er et tall. Hvis ikke, skal funksjonen returnere en passende feilmelding.


import math

def findArea(radius):
        try:
                radius = float(radius)                  #Hvis det er ikke et tall den skal gå linje 19 for håndtering
                if radius < 0:                          #Hvis talle er negativt det kommer feilmelding
                        print("Vennligst skriv inn et positivt tall")
                else:
                        area = math.pi * radius**2
                        print(f"Arealet av sirkelen {area}")
        except ValueError:
                print("Vennligst skriv inn et tall")


skrivRadius = input("Vennligst skriv inn radius: ")     #Jeg vil input fra brukeren
findArea(skrivRadius)                                   #Jeg kaller funksjonen min




