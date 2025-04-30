#Arbeidskrav 1•Innlevering: Uke 37, fredag 15.september 2023•

#Oppgave 1
# 1.Skriv et program som leser inn et navn og skriver ut en hilsen til brukeren. # Eks «Hei, Ola»
navn = input("Vennligst skriv inn ditt navn: ")
print("Hei,", navn.title())


# 2.Skriv et program som leser inn et tall og skriver ut om tallet er positivt, negativt eller null
tall = float(input("Vennligst skriv inn et tall: "))

if tall==0:
    print("Tallet er zero")
elif tall<0:
    print("Tallet er negativt")
else:
    print("Tallet er positivt")


# 3.Skriv et program som leser inn et tall og skriver ut det dobbelte.
tall = float(input("Vennligst skriv inn et tall: "))
print("Resultatet er =", 2*tall)


# 4.Skriv et program som leser inn en tekst og skriver ut teksten baklengs.
text = input("Vennligst skriv inn en text: ")
print("Teksten baklengs:", text[::-1])
