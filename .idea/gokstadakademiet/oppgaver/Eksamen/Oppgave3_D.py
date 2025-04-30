#Oppgave - 3


#3.D - Lag en funksjon som finner ut bokstaven som forekommer oftest i setningen. Funksjonen skal
#ta imot en tekstreng som argument. Funksjonen skal returnere en tuple der det første
#elementet er bokstaven som forekommer oftest, og det andre elementet er antall ganger
#denne bokstaven forekommer i teksten. Merk
#• Du skal kun vurdere bokstaver, og ikke whitespace eller spesialtegn.
#• Hvis det er flere bokstaver med samme høyeste frekvens, kan du returnere en av dem.
#• Behandle store og små bokstaver som samme bokstav (dvs. 'A' og 'a' skal betraktesmsom identiske)


def finnTalletBokstavInSetning():
        tekst = input("Vennligst skrivv inn en tekstreng :")        #Jeg vil input fra brukeren

        nyTekst = ''.join(filter(str.isalpha, tekst.lower()))       #jeg converterer input til småll bokstaver og får som er bokstav


        bokstavList = {}                                #Jeg opprettet en empty tuple
        for bokstav in nyTekst:
                if bokstav in bokstavList:
                        bokstavList[bokstav] += 1       #hvis det finnes forekomsten av bokstav øker
                else:
                        bokstavList[bokstav] = 1        #hvis ikke finnes forekomsten av bokstav blir 1


        oftestForekommendeBokstav = max(bokstavList, key=bokstavList.get)
        oftestForekommendeTall = bokstavList[oftestForekommendeBokstav]

        return (oftestForekommendeBokstav, oftestForekommendeTall)


result = finnTalletBokstavInSetning()
print("Bokstaven som forekommer oftest og antall ganger denne bokstaven forekommer i teksten :", result)
