#Lag en calculator
import time


def skriv_tall():
    tall1 = float(input("Vennligst skriv inn første tallet: "))
    tall2 = float(input("Vennligst skriv inn andre tallet: "))
    return tall1, tall2



def kalkulator():
    choose=input("Vennligst skriv inn hva vil du gjøre: "+
             "\nEnter 1 for Addisjon (Pluss) " +
             "\nEnter 2 for Subtraksjon (Minus) "+
             "\nEnter 3 for Multiplikasjon " +
             "\nEnter 4 for Divisjon " +
             "\nEnter 5 for Avslutt ")

    if choose=="1":
        tall1, tall2 = skriv_tall()
        print(tall1, "+", tall2, "=", (tall1 + tall2))

    elif choose=="2":
        tall1, tall2 = skriv_tall()
        print(tall1, "-", tall2, "=", (tall1 - tall2))

    elif choose=="3":
        tall1, tall2 = skriv_tall()
        print(tall1, "*", tall2, "=", (tall1 * tall2))

    elif choose=="4":
        tall1, tall2 = skriv_tall()
        if(tall2 != 0):
            print(tall1, "/", tall2, "=", (tall1 / tall2))
        else:
            print("Et tall kan ikke deles med 0 !")
            fortsett = input("Hvis du vil prøve igjen trykk 'ja': ").lower()
            while fortsett=="ja":
                time.sleep(2)
                print("Nå kommer en kalkulator programmet...")
                kalkulator()

    elif choose=="5":
        print("Du har avsluttet programmet...")
    else:
        fortsett = input("Du har valgt invalid operasjon. Hvis du vil prøve igjen trykk 'ja': ").lower()
        while fortsett=="ja":
            time.sleep(2)
            print("Nå kommer en kalkulator programmet...")
            kalkulator()



print("Nå kommer en kalkulator programmet...")
time.sleep(3)
kalkulator()