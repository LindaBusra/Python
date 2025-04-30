fornavn = "Ola"
etternavn = "Nordman"
alder =43
print("mit navn er " + fornavn + " " + etternavn + " og jeg er " , alder, " ar gammel")
print("mit navn er " , fornavn , " " + etternavn , " og jeg er " , alder, " ar gammel")
print("mit navn er " + fornavn + " " + etternavn + " og jeg er " + str(alder) + " ar gammel")


tall1 = input("Skriv inn det første tallet: ")
tall2 = input("Skriv inn det andretallet: ")
resultatet =  int(tall1) + int(tall2)

print( tall1 + " + " + tall2 + " = " ,  resultatet)
print( tall1 , "+" , tall2 , "=" ,  resultatet)



tall1= float(input("Skriv in tall1: "))
tall2= float(input("Skriv in tall2: "))

gjennomsnitt = (tall1+tall2)/2
print("Gjennomsnittet av tallene er: ", gjennomsnitt)


lengde = float(input("Skriv inn lengden: "))
bredde = float(input("Skriv inn bredden: "))

areal = lengde * bredde
print("Arealet av rektangelet er: ", areal)