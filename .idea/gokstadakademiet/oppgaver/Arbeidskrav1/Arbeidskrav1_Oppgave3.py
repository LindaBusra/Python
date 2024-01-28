#Arbeidskrav 1•Innlevering: Uke 37, fredag 15.september 2023•

#Oppgave 3
#1. Lag en liste som innholder fem valgfrie dyr (tekststrenger). Skriv så ut alle elementene på hver sin linje.
dyr_list=["fisk", "katt", "kanin", "elefant", "hest"]

for dyr in dyr_list:
    print(dyr)




#2. Deretter skal du gi dyrene navn. Navnene skal du legge i en ny liste. Skriv så ut navnet på
#dyret og hvilken type dyr det er. Eks: «Ola er en hund»
navn_list =["Emily", "Mike", "Tom", "Jack", "Anna"]


for i in range(0, len(dyr_list)):
   print(navn_list[i], "er en", dyr_list[i])




#3. Skriv ut det første og siste elementet i listen med dyr.
print("Det første elementet i liste:", dyr_list[0])
print("Det siste elementet i liste:", dyr_list[-1])




#4. Skriv ut listen med dyr i reversert alfabetisk rekkefølge.
dyr_list.sort()
dyr_list.reverse()
print("Listen med dyr i reversert alfabetisk rekkefølge:", dyr_list)




#5. Du skal nå lage en dictionary med disse fem dyrene med navn. Du kan bruke navn som key og
#hvilken type dyr som value. Skriv så ut navnet på dyret og hvilken type dyr det er. Eks: «Siri er en katt»

dyr_list=["fisk", "katt", "kanin", "elefant", "hest"]
navn_list =["Emily", "Mike", "Tom", "Jack", "Anna"]

dyr_dict = {}  # Opprett en tom dictionary


for i in range(len(dyr_list)):
    navn = navn_list[i]
    dyr_type = dyr_list[i]
    dyr_dict[navn] = dyr_type
    print(f"{navn} er en {dyr_type}")


for navn, dyr_type in dyr_dict.items():
    print(f"{navn} er en {dyr_type}")

