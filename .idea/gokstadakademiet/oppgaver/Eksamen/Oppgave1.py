#Oppgave 1

#Oppgave 1a - Skriv et program som ber brukeren om deres alder. Programmet skal deretter skrive ut alderen til konsoll.

def skrivAlder():
    try:
        alder = float(input("Vennligst skriv inn din alder: "))   #Her får jeg svaret i String format, så converterer jeg den til float i tilfelle noen skriver 14,5 som alder.
        print("Din alder er:", alder)
    except ValueError:                                            #Hvis brukeren skriver noe annet en tall håndterer det med except.
        print("Prøv å skrive et tall...")

print("For Oppgave 1-a: ")
skrivAlder()            #jeg kaller funksjonen min
print()




# #Oppgave 1b - Les inn et heltall fra tastaturet og skriv det ut til konsoll. Hvis brukeren ikke taster inn et
# heltall, skal programmet gi en feilmelding og avsluttes.

def skrivHeltTall():
    try:
        tall = int(input("Vennligst skriv inn et heltall: "))   #Svar tas in String format. Jeg converterer den til integer siden oppgaven vil et helttall.
        print("Tallet du har skrevet: ", tall)
    except ValueError:                                          #Hvis brukeren har ikke skrevet helt tall håndterer det med except.
        print("Prøv å skrive helt tall...")


print("For Oppgave 1-b: ")
skrivHeltTall()
print()




# #Oppgave 1c - Skriv et program som ber brukeren om å skrive inn to tall, summerer disse og skrive resultatet til konsoll.

def summerToTall():
    try:
        tall1 = float(input("Vennligst skriv første tallet: "))     #I tilfelle brukeren skriver number i decimal format, converterer jeg den i float format
        tall2 = float(input("Vennligst skriv andre tallet: "))
        total = tall1 + tall2
        print("Resultat--> ", tall1, " + ", tall2, " = ", total)
    except ValueError:                                              #Hvis brukeren skriver noe annet en tall håndterer det med except.
        print("Prøv å skrive tall...")

print("For Oppgave 1-c: ")
summerToTall()
print()




#Oppgave 1d - Skriv et program som ber brukeren om å taste inn en setning. Programmet skal deretter
#skrive ut hvor mange ord setningen består av.

def hvorMangeOrdISetning(setning):

    ordList = setning.split()   #split() separerer setningen og returnerer den in en liste
    ordNumber = len(ordList)    #med len() får jeg lengden av lista mi
    print("Det finnes ", ordNumber, " ord i setningen din.")


print("For Oppgave 1-d: ")
dinSetning = input("Vennligst skriv inn en setning: ")
hvorMangeOrdISetning(dinSetning)
print()




# #Oppgave 1e - Fortsett programmet fra (D). Denne gang skal programmet skrive ut det lengste ordet i setningen.

def lengsteOrd(setning):

    ordList = setning.split()
    lengsteOrd = ""

    for ord in ordList:
        if len(ord) > len(lengsteOrd):       #Jeg gjør sammenligning med lengde, hvis det er sånn, lengsteOrd er ord
            lengsteOrd = ord

    print("Det lengste ordet er:", lengsteOrd)


print("For Oppgave 1-e: ")
lengsteOrd(dinSetning)
print()




# Oppgave 1f - Fortsett programmet fra (E). Nå skal programmet skrive ut den omvendte setningen. F.eks.
# hvis brukeren skrev inn "Python er gøy", skal programmet skrive ut "gøy er Python".

def omvendtSetningen(setning):

    ordList = setning.split()
    omvendtSetning = ' '.join(reversed(ordList))
    print("Den omvendte setningen er:", omvendtSetning)


print("For Oppgave 1-f: ")
omvendtSetningen(dinSetning)
print()
