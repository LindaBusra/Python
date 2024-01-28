#by Morten Christoffer dahl Hansen

print("Velkommen til min super-quiz!")
name = input("Hva heter du? ")
print(f'Den er god {name}. Da starter vi. Du får fem spørsmål med alternativer og vi ønsker at du svarer på spørsmålene med alternativet som du mener er riktig. \n')
spm = ["Hva er summen av 5*5?","Hvor mange år varer backend-utdanningen på Gokstad?","Hva er tyngst av ett kilo jern og ett kilo med fjær?","Hva heter Kygo til fornavn?","Hvilken farge er det på huden til isbjørnen?"]
alternativ = [["A) 10. ", "B) 20.", "C) 25."], ["A) 1 år. ", "B) 2 år.", "C) 3 år."],["A) jern.", "B) fjær.", "C) Like tungt."],["A) Kyrre.", "B) Kevin.", "C) Gustav."],["A) Svart.", "B) Hvit.", "C) Brun."]]
answer = ["C", "B","C","A","A"]
total = 0
def sporsmalene(sporsmal, alternativ, answer):
    run = True
    while run:
        print(sporsmal, "\n")
        print(f'Her er alternativene du kan velge mellom {" ".join(alternativ)}')
        svar = input("Hva velger du? ")
        if svar.upper() == answer:
            print("Riktig!")
            run = False
            return (1)

        else:
            ny_forsok = input("Det var feil. Vil du prøve igjen? ")
            if ny_forsok.upper() == "JA":
                pass
            else:
                run = False
                return (0)

for i in range(0,5):
    total += sporsmalene(spm[i], alternativ[i], answer[i])
print("\n")
print(f'Bra {name} fikk totalt {total} poeng av {len(spm)} mulige!')