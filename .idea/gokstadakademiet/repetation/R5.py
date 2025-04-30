#Oppgave 11

def lagre_og_les(navn_liste, filnavn):
    with open(filnavn, 'w') as f:          #then lukker også koden. du tenger ikke å tenke lukke
        for navn in navn_liste:
            f.write(navn + '\n')

    with open(filnavn, 'r') as file:
        innhold = file.readlines()


    return [navn.strip() for navn in innhold]

navnene = ["Anna", "Erik", "Jonas", "Linda"]
lagret_navn = lagre_og_les(navnene, "navn.txt")
print(lagret_navn)
