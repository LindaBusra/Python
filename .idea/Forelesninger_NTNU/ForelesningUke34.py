# Input, her er de "hardkodet"
a = 1
b = -2
c = -3

# Utregninger med mellomlagring.
D = b**2 - 4 * a * c
d = D**0.5

x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)
x3 = 4.37
x4 = 2
y = 1.23e-3

# Output
print(x1)
print(x2)
print(x3*100)
print(x4**3)

print(y)

#Datatype: Tekst
text='Hei'
print(text)
text="Hei"
print(text)

## triple-dobbelfnutter. Denne er mer "special". Den kan skrives over flere linjer
enLitenTekst = """19. august 2024
Jeg har det fint!

Hilsen Dag Olav"""
print(enLitenTekst)