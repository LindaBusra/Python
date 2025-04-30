import time

quiz_list = [
    ("1- Hvilket år ble Norge en selvstendig nasjon?: ", "1814"),
    ("2- Hvem malte Mona Lisa?: ", "leonardo da vinci"),
    ("3- Hva er Norges lengste elv?: ", "glomma"),
    ("4- Hva er hovedstaden i Tyrkia?: ", "ankara"),
    ("5- Hva er navnet på den norske forfatteren som skrev romanen 'Hunger'?: ", "knut hamsun"),
    ("6- Hvilken norsk eventyrfigur er kjent for å ha en tannfe som bytter ut barnas mistede tenner med penger?: ", "askeladden"),
    ("7- Hvilken norsk by er kjent for sin årlige 'Vikingfestival'?: ", "lofoten"),
    ("8- Hvilken planet i solsystemet vårt kalles 'den røde planeten'?: ","mars"),
    ("9- Hvilket land er kjent som 'Smørbrødlandet'?: ", "danmark"),
    ("10- Hvem skrev boken 'Romeo og Julie'?: ", "william shakespeare")
]

print("Det er en liten Quiz, vennligst svar spørsmålene, hvis det er noen spørsmål som du vill hoppe over trykk 'H':")
time.sleep(2)
print("Det kommer spørsmål...")
time.sleep(2)


def quiz():
    poeng="Du har fått 10 poeng"
    igjen="Prøv sjansen med neste spørsmål"
    sum=0

    for spørsmål, rett_svar in quiz_list:
        svar = input(f"{spørsmål}").lower()
        if svar != "h":

            if svar == rett_svar:
                print(poeng)
                sum +=10
            else:
                if spørsmål != "Hvem skrev boken 'Romeo og Julie'?: ":
                    print(igjen)
                else:
                    break

    time.sleep(2)
    print("Poenget ditt regnes...")
    time.sleep(2)

    str ="Etter quiz poengen din er: "

    if sum<50 and sum>20:
        print(str, sum, "Prøv å lese mer!")
    elif sum>= 50 and sum<=70:
        print(str, sum, "Du er god nok...")
    elif sum>70 and sum<=90:
        print(str, sum, "Du er kjempe good :)")
    elif sum>90:
        print(str, sum, "Du er supert :) ")
    else:
        time.sleep(2)
        print(str, sum)
        fortsett = input("Hvis du vil prøve igjen trykk på 'y': ").lower()
        if fortsett=='y':
            time.sleep(2)
            print("Det kommer spørsmål...")
            time.sleep(2)
            quiz()

quiz()
