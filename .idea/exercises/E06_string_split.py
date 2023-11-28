

#add string with triple quotes if you have a long text
text = """Norge, Noreg, er et monarki i Europa som utgjør den vestlige og nordlige delen av Den skandinaviske halvøya. Landet grenser i øst mot Sverige, Finland og Russland. I nord, vest og sør er Norge omgitt av hav: Barentshavet i nordøst, Norskehavet i nordvest, Nordsjøen i vest og sørvest og Skagerrak i sørøst.
I tillegg omfatter Norge øygruppen Svalbard (inkludert Bjørnøya) og Jan Mayen i det nordlige Atlanterhavet, likeledes tre biland: Bouvetøya i det sørlige Atlanterhavet, Peter I Øy i det sørlige Stillehavet og Dronning Maud Land som utgjør en sektor av Antarktis sør for Atlanterhavet.
Norge er et langt og smalt land, med en svært lang kystlinje. Arealet i hovedlandet er 323 806 kvadratkilometer, 384 483 kvadratkilometer inkludert Svalbard og Jan Mayen, og landet er henholdsvis nr. 8 og nr. 6 blant Europas land etter areal. Med en befolkning på om lag 5,5 millioner innbyggere (2023) gjør dette Norge til et relativt tynt befolket land.
Norge er et av verdens rikeste land. Dette skyldes blant annet tilgang til flere energikilder: vannkraft, olje og gass. Landet har en sterk industrialisering, kort avstand til viktige markeder i Vest-Europa, politisk stabilitet, godt utbygd infrastruktur og en befolkning med et høyt utdanningsnivå.
Navnet Norge har norrøn opprinnelse; den tradisjonelle og i dag vanligste forklaringen, er at det er dannet av norðr, 'nord', og vegr, 'vei' eller 'lei', det vil si ‘nordveien’ eller ‘veien mot nord’. Dette ligger til grunn for de aller fleste vesteuropeiske navneformene, eksempelvis Norway (engelsk), Norwegen (tysk), Norvège (fransk). Vedrørende andre forklaringer, se Norge/Noreg – etymologi."""


print(text)
print("number of character:",len(text))  #number of character
print(text.split())  #split the text with space
print("number of word:",len(text.split())) # number of word



#how many times a particular word appears
word = "Norge"
count=0
for i in text.split():
    if i==word:
        count+=1

print(count,"times we have", word)




#how many times "a or A" appears
text = "a b c A a b"
print(len(text.split()))
print(text.split())


#1.way
count =0
for i in text.split():
    if i=="a":
        count +=1
print(count)



#2.way
word_count={}
for word in text.lower().split():
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1

print(word_count)




#how many times "a or A" appears
text = """Norge, Noreg, er et monarki i Europa som utgjør den vestlige og nordlige delen av Den skandinaviske halvøya. Landet grenser i øst mot Sverige, Finland og Russland. I nord, vest og sør er Norge omgitt av hav: Barentshavet i nordøst, Norskehavet i nordvest, Nordsjøen i vest og sørvest og Skagerrak i sørøst.
I tillegg omfatter Norge øygruppen Svalbard (inkludert Bjørnøya) og Jan Mayen i det nordlige Atlanterhavet, likeledes tre biland: Bouvetøya i det sørlige Atlanterhavet, Peter I Øy i det sørlige Stillehavet og Dronning Maud Land som utgjør en sektor av Antarktis sør for Atlanterhavet.
Norge er et langt og smalt land, med en svært lang kystlinje. Arealet i hovedlandet er 323 806 kvadratkilometer, 384 483 kvadratkilometer inkludert Svalbard og Jan Mayen, og landet er henholdsvis nr. 8 og nr. 6 blant Europas land etter areal. Med en befolkning på om lag 5,5 millioner innbyggere (2023) gjør dette Norge til et relativt tynt befolket land.
Norge er et av verdens rikeste land. Dette skyldes blant annet tilgang til flere energikilder: vannkraft, olje og gass. Landet har en sterk industrialisering, kort avstand til viktige markeder i Vest-Europa, politisk stabilitet, godt utbygd infrastruktur og en befolkning med et høyt utdanningsnivå.
Navnet Norge har norrøn opprinnelse; den tradisjonelle og i dag vanligste forklaringen, er at det er dannet av norðr, 'nord', og vegr, 'vei' eller 'lei', det vil si ‘nordveien’ eller ‘veien mot nord’. Dette ligger til grunn for de aller fleste vesteuropeiske navneformene, eksempelvis Norway (engelsk), Norwegen (tysk), Norvège (fransk). Vedrørende andre forklaringer, se Norge/Noreg – etymologi."""

word_count={}
for word in text.lower().split():
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word]=1

print(word_count)