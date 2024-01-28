#min version

#• Lag et program som ber brukeren om lese inn en kommaseparert linje med tall fra en fil "tall.csv"
#og legge disse i en liste. Eksempel på fil innhold: 12, 15, 8.5, 20, 7


#I created a function for read this csv file:
new_data =[]

def read_file():
    with open("tall.csv", encoding = "utf-8-sig") as fil:
        innhold = fil.read().strip()
        new_data = innhold.split(",")

    print(new_data)

    #if I will get the elements one by one
    for i in new_data:
        print(i)

#I called function
read_file()


#Programmet skal deretter be brukeren om å taste inn et annet tall kalt "deleren".


def hva_vil_du():

    while True:
        svar = input("Hvis vil du prøve igjen, enter 'Ja'. For å avslutte, enter 'Nei': ").lower()
        if svar == 'ja':
            skriv_tall()
        else:
            break

def skriv_tall():
    global new_data
    while True:
        try:
            tall = int(input("Vennligst skriv inn et tall: "))
            if tall == 0:
                raise ZeroDivisionError("Du kan ikke dele et tall på null")
            resultat = [i / tall for i in new_data]
            print("Resultater etter deling:")
            for r in resultat:
                print(r)
        except ZeroDivisionError as e:
            print(str(e))
            hva_vil_du()
        except ValueError:
            print("Dette inkluderer ikke tall!")
            hva_vil_du()
        else:
            hva_vil_du()

def main():
    global new_data
    # Les kommaseparerte tall fra filen
    with open("tall.csv", encoding="utf-8-sig") as fil:
        data = fil.read().strip()
        new_data = [float(t) for t in data.split(",")]

    print("Tall fra filen:", new_data)

    hva_vil_du()

if __name__ == "__main__":
    main()

