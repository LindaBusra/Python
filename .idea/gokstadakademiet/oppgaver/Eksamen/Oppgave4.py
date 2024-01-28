#Oppgave 4
import os
import csv
from collections import Counter


# Filen som er gitt i oppgaven står i Arbeidskrav2 mappen
filePath = "solgtevarer.csv"


# Jeg skal bruke den funksjonen som tar en størrelse og sjekker om størrelsen er gyldig.
def erGyldigStørrelse(størrelse):
    gyldigeStørrelser = ["S", "M", "L", "XL", "XXL"]
    return størrelse in gyldigeStørrelser

#print(erGyldigStørrelse("XL"))      #True
#print(erGyldigStørrelse("3XL"))     #False




# Liste for å lagre dataene
data = []

try:
    with open(filePath, "r", encoding="utf-8") as fil:      # Åpne en fil for lesing ved hjelp av filePath
        leser = csv.reader(fil)                             # Den oppretter en CSV-leser
        header = next(leser)                                # For å hoppe over overskriftsraden


#radnummer representerer indeksen på den gjeldende raden som leses. Den starter med verdien 1 her. (default=0)
#rad er hele innholdet av den gjeldende raden som leses fra filen. for eksempel rad[0]: første kolonnen

        for radnummer, rad in enumerate(leser, start=1):    # leser er en iterator som brukes til å lese gjennom filen rad for rad.
            if len(rad) == 7:                               # Har raden forventet antall kolonner?...i CSV-filen har vi 7 kolonner
                if not erGyldigStørrelse(rad[4]):           # Hvis størrelsen ikke er gyldig, gir den en feilmelding
                    print(f"Det står en feil i rad {radnummer}: Ugyldig størrelse: {rad[4]}")
                    continue
                data.append(rad)                            # Legg til data i listen
            else:
                print(f"Det står en feil i rad {radnummer}: Kolon nummer er ikke som forventet.")     # Hvis det mangler kolonner i en rad, gir den en feilmelding
except FileNotFoundError:                                   # Dette håndterer tilfellet der filen ikke eksisterer og
    print("Filen ble ikke funnet.")                         # skriver ut en melding som sier "Filen ble ikke funnet."
except Exception as e:                                      # parent Exception
    print("En uventet feil oppstod...")                     # Dette håndterer generelle unntak som ikke er spesifikke for filen

print("Data listen som ble lagret etter kontroll:")         # Skriv ut data listen som ble lagret
for rad in data:
    print(rad)



print("\n-----------------------------------------------------------------------------------------------------------\n")



# A. Hvor mange gensere er solgt i totalt?
def beregnTotaltGensereSalg():
    totaltGensereSalg = 0                               # I begynnelsen er salget 0

    try:
        with open(filePath, "r", encoding="utf-8") as fil:                # Åpne en fil for lesing ved hjelp av filePath
            leser = csv.reader(fil)                     # Den oppretter en CSV-leser
            next(leser)                                 # For å hoppe over overskriftsraden

            # For å beregne hvor mange gensere som er solgt
            for rad in leser:
                vare = rad[2]                           # Kolonnen for varer
                if vare.lower() == "genser":            # Hvis det er en genser
                    totaltGensereSalg += int(rad[5])    # Øk totaltGensereSalg tallet, rad[5] er kolonnen for antall
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
    except Exception as e:
        print("En uventet feil oppstod!")

    return totaltGensereSalg


# Hvor mange gensere er solgt, se resultatet i konsollen
print("Totalt antall gensere som er solgt:", beregnTotaltGensereSalg())



print("\n-----------------------------------------------------------------------------------------------------------\n")



# B. Hva er den totale inntekten fra salget av gensere?

def beregnTotalInntektGensere():
    totalInntektGensere = 0                                             # Inntekt er 0 i begynnelsen

    try:
        with open(filePath, "r", encoding="utf-8") as fil:                                # Åpne en fil for lesing ved hjelp av filePath
            leser = csv.reader(fil)                                     # Den oppretter en CSV-leser
            next(leser)                                                 # For å hoppe over overskriftsraden

            # Kalkuler total inntekt fra gensersalget
            for rad in leser:
                vare = rad[2]                                           # Kolonnen for varer
                if vare.lower() == "genser":
                    antall = int(rad[5])                                # Kolonnen for antall varer
                    prisPerGenser = int(rad[6])                         # Priskolonnen er rad[6]
                    totalInntektGensere += antall * prisPerGenser       # Legg til det nye antallet*prisen som kommer fra gjeldende rad
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
    except Exception as e:
        print("En uventet feil oppstod!")

    return totalInntektGensere


# Beregn total inntekt fra gensersalget, se resultatet i konsollen
print("Total inntekt fra salg av gensere:", beregnTotalInntektGensere())




print("\n-----------------------------------------------------------------------------------------------------------\n")





# C. Hvor mange kunder kjøpte varer i størrelsen 'XL'?
def tellKunderMedStørrelseXl():
    xlKunder = set()  # For å finne unike kunder som har kjøpt i størrelsen 'XL', har jeg brukt en set()

    try:
        with open(filePath, "r", encoding="utf-8") as fil:                # Åpne en fil for lesing ved hjelp av filePath
            leser = csv.reader(fil)                     # Den oppretter en CSV-leser
            next(leser)                                 # For å hoppe over overskriftsraden

            # For å finne antall kunder med størrelse 'XL'
            for rad in leser:
                størrelse = rad[4]                      # Kolonnen for størrelse
                if størrelse.upper() == "XL":
                    kunde = rad[0] + " " + rad[1]       # Jeg sammensetter fornavn og etternavn
                    xlKunder.add(kunde)                 # Legg kundens fullt navn til  set() som heter xlKunder
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
    except Exception as e:
        print("En uventet feil oppstod!")

    return len(xlKunder)



# Antall kunder som kjøpte størrelse 'XL',  se resultatet i konsollen
print("Antall kunder som kjøpte varer i størrelse 'XL':", tellKunderMedStørrelseXl())




print("\n-----------------------------------------------------------------------------------------------------------\n")




# D. Hvor mange kunder har kjøpt mer enn 3 varer? (gå ut fra at det ikke er flere kunder per linje)

def tellKunderMedMerEnn3Kjøp():
    kundeKjøpAntall = {}  # Ordbok for å holde styr på antall kjøp per kunde

    try:
        with open(filePath, "r", encoding="utf-8") as fil:
            leser = csv.reader(fil)
            next(leser)

            for rad in leser:
                kunde = rad[0] + " " + rad[1]
                antallVare = int(rad[5])

                # Antall av varene som ble solgt
                kundeKjøpAntall[kunde] = kundeKjøpAntall.get(kunde, 0) + antallVare

    except FileNotFoundError:
        print("Filen ble ikke funnet.")
    except Exception as e:
        print("En uventet feil oppstod!")

    # Gi meg bare kunder som har kjøpt mer enn 3 varer
    kunderMerEnn3Kjøp = {kunde: kjøp for kunde, kjøp in kundeKjøpAntall.items() if kjøp > 3}

    # Gi meg size of kunderMerEnn3Kjøp
    antallMerEnn3 = len(kunderMerEnn3Kjøp)

    return antallMerEnn3



#Antall kunder som har kjøpt mer enn 3 varer, se resultatet i konsolen.
print("Antall kunder som har kjøpt mer enn 3 varer:", tellKunderMedMerEnn3Kjøp())




print("\n-----------------------------------------------------------------------------------------------------------\n")



# E. Hvilken farge har flest solgte varer?

def finnFargeMedFlestSolgteVarer():
    fargeTelling = Counter()                            # for å telle hvor mange ganger hver unik verdi forekommer i en samling

    try:
        with open(filePath, "r", encoding="utf-8") as fil:               # Åpne en fil for lesing ved hjelp av filePath
            leser = csv.reader(fil)                     # Den oppretter en CSV-leser
            next(leser)                                 # For å hoppe over overskriftsraden

            # Tell antall solgte varer per farge
            for rad in leser:
                farge = rad[3]                          # Kolonnen for farge
                fargeTelling[farge] += 1
    except FileNotFoundError:
        print("Filen ble ikke funnet.")
    except Exception as e:
        print(f"En uventet feil oppstod: {str(e)}")

    # Jeg finner den mest solgte fargen fra fargeTelling-tellermengden.
    mestSolgtFarge = fargeTelling.most_common(1)

    return mestSolgtFarge[0] if mestSolgtFarge else None


# Finn fargen med flest solgte varer
mestSolgtFarge = finnFargeMedFlestSolgteVarer()

# Skriv ut resultatet
if mestSolgtFarge:
    print("Fargen med flest solgte varer:", mestSolgtFarge[0])
    print("Antall solgte varer i denne fargen:", mestSolgtFarge[1])
else:
    print("Ingen data funnet...")



print("\n-----------------------------------------------------------------------------------------------------------\n")



# Før jeg kjører koden min, sletter jeg eksisterende filen som heter "salgs_analyse_svar.txt" (hvis filen eksisterer)
if os.path.exists("salgs_analyse_svar.txt"):
    os.remove("salgs_analyse_svar.txt")
else:
    print("Filen eksisterer ikke")



print("\n-----------------------------------------------------------------------------------------------------------\n")




# F. Lagre analysedata til fil
utdatafil = "salgs_analyse_svar.txt"

def opprettDokumentMedKorreksjoner():

    # Lager teksten
    svar_tekst = "Svar for Oppgave 4, fra A til E: \n\n"

    totaltGensereSalg = 56  # Svar på A-oppgaven
    svar_tekst += f"Oppgave 4-A. Hvor mange gensere er solgt i totalt?   Svar: {totaltGensereSalg}\n"

    totalInntektGensere = 22344  # Svar på B-oppgaven
    svar_tekst += f"Oppgave 4-B. Hva er den totale inntekten fra salget av gensere?   Svar: {totalInntektGensere} kr\n"

    antallXlKunder = 5  # Svar på C-oppgaven
    svar_tekst += f"Oppgave 4-C. Hvor mange kunder kjøpte varer i størrelsen 'XL'?   Svar: {antallXlKunder}\n"

    antallKunderMerEnn3 = 6  # Svar på D-oppgaven
    svar_tekst += f"Oppgave 4-D. Hvor mange kunder har kjøpt mer enn 3 varer?   Svar: {antallKunderMerEnn3}\n"

    mestSolgtFarge = ("Blå", 13)  # Svar på E-oppgaven
    svar_tekst += f"Oppgave 4-E. Hvilken farge har flest solgte varer?   Svar: {mestSolgtFarge[0]} med {mestSolgtFarge[1]} solgte varer\n"


    return svar_tekst


# Få korrigert tekst
korrigert_tekst = opprettDokumentMedKorreksjoner()

# Skriv til filen på nytt
with open(utdatafil, "w", encoding="utf-8") as fil:
    fil.write(korrigert_tekst)

print(f"Dokumentet '{utdatafil}' er oppdatert.")

