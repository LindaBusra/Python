# Oppgave 4
tall_str = input("Skriv inn et tall: ")
tall = float(tall_str)

if tall>0:
    print("Tallet er positivt.")
elif tall<0:
    print("Tallet er negativt.")
else:
    print("Tallet er null.")



# Oppgave 5 Lag navn liste
navn_liste = []
for element in range(5):
    navn = input(f"Skriv inn navn {element + 1}: ")
    navn_liste.append(navn)

print(f"Navn_liste {navn_liste}")
print(f"Navnet som vinner er:  {navn_liste[3]}")
