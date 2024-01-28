#Oppgave 1 - La brukeren skriv inn i konsolen navnet sitt
navn = input("Hva er ditt navn?")
hilsen = f"Hei, {navn}"
print(hilsen)



#Oppgave 2 - Skriv to tall og convertere dem decimal
tall1_str =input("Skriv inn det første tallet: ")
tall2_str =input("Skriv inn det andre tallet: ")
tall1 = float(tall1_str)
tall2 = float(tall2_str)

summen = tall1 + tall2
print(f"Først tallet {tall1}, andre tallet {tall2_str}, og summen av tallene er {summen}")



#Oppgave 3 - Skriv in radius for en sirkel
radius_str = input("Skriv inn radius for sirkelen: ")
radius = float(radius_str)

omkrets = 2 * 3.14 * radius
print(f"Omkretsen av sirkelen er: {omkrets}" )