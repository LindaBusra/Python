# oppgave 12

try :
    tall1 = float(input("Skriv inn det første tallet: "))
    tall2 = float(input("Skriv inn det andre tallet: "))
    resultat = tall1 / tall2
    print(resultat)
except ZeroDivisionError:
    print("Du kan ikke dele et tall med null")




# oppgave 13  Betingelse og data strukturer

operasjoner = ["+", "-", "*", "/"]

op = input(f"Velg en operasjon fra {operasjoner} :")
#La brukeren få vite om feil operasjon for de går videre med tall1 og tall2
tall1 = float(input("Skriv inn det første tallet: "))
tall2 = float(input("Skriv inn det andre tallet: "))

#Ersatt  if elif med en linje
if op == "+":
    resultat = tall1 + tall2
elif op == "-":
    resultat = tall1 - tall2
elif op == "*":
    resultat = tall1 * tall2
elif op == "/":
    resultat = tall1 / tall2
else:
    resultat = None

if resultat is not None:
    print(f"Resultatet av {tall1} {op} {tall2} er {resultat}")
else:
    print("Ugyldig operasjon eller deling med null!")
    #Håndter deling på null