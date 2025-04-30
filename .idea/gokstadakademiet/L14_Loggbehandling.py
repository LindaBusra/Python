# Logg behandling, legge til loggmeldinger med tidsstempel
# Med funksjoner som tillater å lese og skrive til filen

import datetime

def legg_til_loggmelding(loggfil, melding):
    tidspunkt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    loggmelding = f"{tidspunkt} : {melding}\n"
    with open(loggfil, 'a') as fil:
        fil.write(loggmelding)


def les_loggmeldinger(loggfil):
    try:
        with open(loggfil, 'r') as fil:
            loggdata = fil.read()
            print(loggdata)
    except FileNotFoundError:
        print("Loggfilen ble ikke funnet")


loggfil = 'logg.txt'

while True:
    print("\n Velg en handling: ")
    print("1. Legg til en loggmelding")
    print("2. Les eksisterende loggmeldinger")
    print("3. Avslutt")

    valg = input("Skrin inn valget ditt: ")

    if valg == '1':
        melding =input("Skriv inn loggmeldingen: ")
        legg_til_loggmelding(loggfil, melding)
        print("Logg melidng er lagt til. ")
    elif valg == '2':
        les_loggmeldinger(loggfil)
    elif valg == '3':
        break
    else:
        print("Ugyldig valg. Prøv igjen...")
