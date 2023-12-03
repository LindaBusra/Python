ola_alder = int(input("Skriv inn Ola sin alder: "))
kari_alder = int(input("Skriv inn Kari sin alder: "))


if ola_alder>kari_alder:
    print("Ola er eldre enn Kari")
elif ola_alder==kari_alder:
    print("Ola og Kari er like gamle")
else:
    print("Kari er eldre enn Ola")




celsius = float(input("Skriv inn temperaturen i Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperaturen i Fahrenheit er: ", fahrenheit)



#spør alder til use, og skriv han er voksen ellelr barn

poeng = int(input("Skriv hva er poenget ditt"))

if poeng>60:
    print("Du får plass i NTNU")
elif poeng>50:
    print("Du får plass i UI")
elif poeng>40:
    print("Du får plass i Høyskolen Vestlandet")
else:
    print("Nei, du må jobbe mer :( ")



print("------------------------------------------------------------")


#Lag en calculator
tall1 = float(input("Skriv inn første tallet: "))
tall2 = float(input("Skriv inn andre tallet: "))

choose=input("Skriv inn hvilke operasjon vil du gjøre: +, -, /, * ")


if choose=="+":
    print(tall1, "+", tall2, "=", (tall1 + tall2))
elif choose=="-":
    print(tall1, "-", tall2, "=", (tall1 - tall2))
elif choose=="*":
    print(tall1, "*", tall2, "=", (tall1 * tall2))
elif choose=="/":
    print(tall1, "/", tall2, "=", (tall1 / tall2))
else:
    print("Du har valgt invalid operasjon, prøv igjen :)")