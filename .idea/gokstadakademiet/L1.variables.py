

from rich.traceback import install
install(show_locals=True)


navn =Alice
print(navn)

#print funksjonen
navn = "Alice"
print("Hei, " + navn + "!")


#input funksjonen
alder = input("Hvor gammel er du?")
print("Du er " + alder + " år gammel.")



#Casting
tall_streng = "42"
tall_heltall = int(tall_streng)
print(tall_heltall + 5)     #output = 47




x=5
print(x)

y="Mike"
print(y)

z=4.0
print(z)

print(x,y,z)
print(str(x) + y + str(z))




x = 10
y = 3
sum = x+ y
print(sum)
resultat = x ** y   #10^3 = 1000
print(resultat)



#Mathematical operatorer
# +  addisjon, -substraksjon, *multiplikasjon, / divisjon, % modulus, ** eksponent


#Sammenligninsoperatorer
#== likhet, !=ikke likhet
#< mindre enn, > større enn
#<= mindre enn eller lik, >= større enn eller lik

alder = 25
er_voksen = alder >= 18
print(er_voksen)    #Resultat: True


#Logiske operatorer
#and(og), or(eler), not(ikke)
x= 5
y = 10
resultat = x<y and y> 7   #True
print(resultat)

print("-------------------------------------------------------------------------------------------")

tall1="42"

tall2= 8

resultatet =int(tall1) + tall2
print("Resultatet er = ",  resultatet)





