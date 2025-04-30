#Oppgave - 3


#3.B - Skriv en funksjon som konverterer meter til kilometer. Funksjonen skal ta imot antall meter
#som argument og returnere tilsvarende antall kilometer. Den bør også sjekke at inndataen er
#positiv og er et tall. Hvis ikke, skal funksjonen returnere en passende feilmelding.
print("For Oppgave 3.B: ")

def meterTilKilometer(meter):
        try:
                meter = float(meter)                    #Hvis det er ikke et tall den skal gå linje 16 for håndtering
                if meter < 0:                           #Hvis talle er negativt det kommer feilmelding
                        print("Vennligst skriv inn et positivt tall")
                else:
                        print(f"{meter} meter er {meter / 1000} kilometer")
        except ValueError:
                print("Vennligst skriv inn et tall")



skrivMeter = input("Vennligst skriv inn meter: ")       #Jeg vil input fra brukeren
meterTilKilometer(skrivMeter)                           #Jeg kaller funksjonen min



