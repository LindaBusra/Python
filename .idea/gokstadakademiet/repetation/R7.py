# oppgave 18
#Lage en quiz
sporsmaal = [
    {
        "tekst" : "Hva er hovedstaten i Norge?",
        "valg" : ["Oslo", "Bergen", "Trondheim", "Kristiansand"],
        "svar" : "Oslo"
    },
    {
        "tekst" : "Hvilket språk snakker de i Brasil?",
        "valg" : ["Engelsk", "Spansk", "Portugisisk", "Fransk"],
        "svar" : "Portugisisk"
    },
    {
        "tekst" : "Hvilket dyr er kjent som 'Kongen var jungelen' ?",
        "valg" : ["Elefant", "Tiger", "Giraff", "Løve"],
        "svar" : "Løve"
    }
]

riktige_svar = 0

for spm in sporsmaal:
    print(spm["tekst"])
    for i, valg in enumerate(spm["valg"]):
        print(f"{i + 1}. {valg}")
    svar = int(input("Ditt valg (1-4): "))
    if spm["valg"][svar-1] == spm["svar"]:
        riktige_svar += 1

if riktige_svar == 3:
    print("Gratulerer! Alle svarene er riktige!")
elif riktige_svar == 2:
    print("Bra jobba! Du får C på eksamen!")
else:
    print("Prøv igjen senere!")








