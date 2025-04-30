import datetime
import math

# 1 Be brukeren om sitt navn og skriv ut en hilsen med navnet.

navn = input("Vennligst skriv inn ditt navn: ")
print("Hei", navn.title(), "\b! Så hyggelig å se deg:) ")


# 2 Be brukeren om to tall, legg dem sammen, og skriv ut resultatet.
tall1= int(input("Vennligst skriv inn tall 1: "))
tall2= int(input("Vennligst skriv inn tall 2: "))
print("Total er:", (tall1+tall2))


# 3 Be brukeren om to tall og finn gjennomsnittet av dem. Skriv ut resultatet.
tall1= float(input("Vennligst skriv inn tall 1: "))
tall2= float(input("Vennligst skriv inn tall 2: "))
print("Gjennomsnittet av dem:", (tall1+tall2)/2)


# 4 Konverter en temperatur fra Celsius til Fahrenheit og skriv ut resultatet.
celsius = 45
fahrenheit = 32 + (celsius * 9/5)
print("Temperaturen i Fahrenheit er: ", fahrenheit)


# 5 La brukeren gi inn et antall minutter og konverter dette til timer og minutter.
antall_minutter =  int(input("Vennligst skriv inn antall minutter: "))
timer= int(antall_minutter/60)
rest_minutter=antall_minutter%60

print(antall_minutter, "minutter er", timer, "timer og", rest_minutter, "minutter")


# 6 Be brukeren om en tekst og tell antall tegn i teksten. Skriv ut resultatet.
txt = input("Vennligst skriv inn din text: ")
print("Det er", len(txt), "tegn i teksten" )



# 7 Spør brukeren om sin fødselsdato og beregn deres alder.

from datetime import datetime

fødselsdato_str= (input("Kan du skrive fødseldatoen din? (Format: År-Måned-Dag, Eksempel: 1938-05-30 "))

fødselsdato = datetime.strptime(fødselsdato_str, "%Y-%m-%d")

now = datetime.now()

alder = int((now-fødselsdato).days / 365)
print("Du er", alder, "gammel år")



# 8 La brukeren gi inn en pris, beregn 15% tips og skriv ut både tips og totalprisen.

pris = int(input("Vennligst skriv inn en pris: "))
tips = pris*0.15
pris += tips
print("Tips:", tips, "og total pris:", pris)



# 9 Be brukeren om et ord, og skriv ut ordet baklengs.
ord = input("Kan du skrive et ord: ")
reverse = ord[::-1]
print("ordet baklengs:", reverse)



# 10 Spør brukeren om en hel streng, og finn ut om strengen er et palindrom.
setning = input("Kan du skrive en setning: ")
reverse = setning[::-1]

if setning==reverse:
    print("Den er palindrome")
else:
    print("Den er ikke palindrome")



# 11 Be brukeren om deres vekt i kilo og høyde i meter, og beregn deres BMI.
vekt = float(input("Skriv inn din vekt (kilo): "))
høyd = float(input("Skriv inn din høyd (meter)"))
bmi = vekt / (høyd*høyd)

print("BMI er:", bmi)

#or with create a function
def bmi(vekt, høyd):
    bmi = vekt / (høyd*høyd)
    return bmi

print("BMI er:", bmi(vekt, høyd))



# 12 Konverter en temperatur fra Fahrenheit til Celsius og skriv ut resultatet.

fahrenheit = 35
celsius = (fahrenheit -32) * 5/9
print("Celsius er: ", celsius)



# 13 Spør brukeren om deres favorittfarge og skriv ut en melding som sier "Din favorittfarge er FARGE".
favorittfarge = input("Vennligst skriv inn din favorittfarge: ")
print("Din favorittfarge er", favorittfarge)
#or
print(f"Din favorittfarge er {favorittfarge}")
#or
print("Din favorittfarge er {}".format(favorittfarge))



# 14 Be brukeren om radiusen på en sirkel og beregn sirkelens omkrets.
radius = float(input("Vennligst skriv inn radius: "))
circumference = 2*3.14*radius
print("Circumference:", circumference)

#or
def circumference_for_sirkel(radius):
    return 2*3.14*radius
print("Circumference:", circumference_for_sirkel(radius))



# 15 Be brukeren om radiusen på en sirkel og beregn sirkelens areal.
radius = float(input("Vennligst skriv inn radius: "))
areal = 3.14*(radius**2)
print("Areal:", areal)

#or
def areal_for_sirkel(radius):
    return 3.14*(radius**2)
print("Areal:", areal_for_sirkel(radius))



# 16 Spør brukeren om sin høyde i cm og konverter den til fot (1 fot =30.48 cm).

høyd= float(input("Vennligst skriv inn din høyde i cm: "))
fot = høyd*30.48
print("Din høyd er:", fot, "fot")



# 17 Be brukeren om to adjektiv, et substantiv og et verb, og lag en setning med disse ordene.
adjektiv1= input("Vennligst skriv inn adjektiv 1: ")
adjektiv2 = input("Vennligst skriv inn adjektiv 2: ")
substantiv = input("Vennligst skriv inn substantiv: ")
verb = input("Vennligst skriv inn verb: ")

print(f"Du er pleier alltid å {verb} {substantiv} med en {adjektiv1} og {adjektiv2} måte ")



# 18 Be brukeren om en tekst og skriv ut den femte bokstaven i teksten.
tekst= input("Vennligst skriv inn tekst: ")
print("Den femte bokstaven i teksten:", tekst[0:5])



# 19 Spør brukeren om en streng, og skriv ut om strengen er kortere, lik eller lengre enn 5 tegn.
tekst= input("Vennligst skriv inn tekst: ")

if len(tekst)<5:
    print("Strengen er kortere enn 5")
elif len(tekst)>5:
    print("Strengen er lengre enn 5")
else:
    print("Strengen er lik 5")



# 20 La brukeren gi inn et beløp i en valuta og konverter dette til en annen valuta basert på en gitt kurs.

beløp =  int(input("Vennligst skriv inn hvor mye kroner du vil konvertere: "))
valuta = input("Vennligst skrivv inn valuta du vil konvert:  dollar-pund-euro-rupi: ").lower()
dollar=10.7055
pund=13.4831
euro=11.5705
rupi=12.956
if valuta=="dollar":
    print("Du har:", dollar, "dollar")
elif valuta=="pund":
    print("Du har:", pund, "pund")
elif valuta=="euro":
    print("Du har:", euro, "euro")
elif valuta=="rupi":
    print("Du har:", rupi, "rupi")
else:
    print("Du har skrevt inn en feil valuta!")



# 21 Spør brukeren om et heltall og skriv ut om tallet er oddetall eller partall.
helttall = int(input("Vennligst skriv inn et heltall: "))

if helttall%2==0:
    print(helttall,"er partall")
else:
    print(helttall,"er oddetall")



# 22 Be brukeren om et ord og skriv ut antall vokaler i ordet.
ord = input("Vennligst skriv inn et ord").lower()
count=0

for i in ord:
    vokal = (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y" or i=="æ" or i=="ø" or i=="å")
    if (vokal):
        count += 1

print("Antall vokaler i ordet: ", count)



# 23 La brukeren gi inn sin fødselsdato og finn ut hvilket stjernetegn de er født under.

setning = input("Vennligst skriv fødselsdatoen din i den format: dag-måned-år (eksempel: 28.8.2010): ")
dag=int(setning.split(".")[0])
måned=int(setning.split(".")[1])

if (dag<=31 and dag>=20 and måned==4) or  (dag<=20 and dag>=1 and måned==5):
    print("Tyren")
elif (dag<=31 and dag>=21 and måned==5) or  (dag<=20 and dag>=1 and måned==6):
    print("Tvilling")
elif (dag<=31 and dag>=21 and måned==6) or  (dag<=22 and dag>=1 and måned==7):
    print("Krepsen")
elif (dag<=31 and dag>=23 and måned==7) or  (dag<=22 and dag>=1 and måned==8):
    print("Løven")
elif (dag<=31 and dag>=22 and måned==8) or  (dag<=21 and dag>=1 and måned==9):
    print("Jomfruen")
elif (dag<=31 and dag>=23 and måned==9) or  (dag<=22 and dag>=1 and måned==10):
    print("Vekten")
elif (dag<=31 and dag>=23 and måned==10) or  (dag<=21 and dag>=1 and måned==11):
    print("Skorpionen")
elif (dag<=31 and dag>=22 and måned==11) or  (dag<=21 and dag>=1 and måned==12):
    print("Skytten")
elif (dag<=31 and dag>=22 and måned==12) or  (dag<=19 and dag>=1 and måned==1):
    print("Steinbukken")
elif (dag<=31 and dag>=20 and måned==1) or  (dag<=18 and dag>=1 and måned==2):
    print("Vannmannen")
elif (dag<=31 and dag>=19 and måned==2) or  (dag<=20 and dag>=1 and måned==3):
    print("Fiskene")
elif (dag<=31 and dag>=21 and måned==3) or  (dag<=19 and dag>=1 and måned==4):
    print("Væren")
else:
    print("Du har skrevet in feil format :(")




# 24 Be brukeren om et tall og skriv ut den kvadratiske roten av tallet.
tall = int(input("Vennligst skriv inn et tall: "))
print("Kvadratiske roten av tallet: ",  math.sqrt(tall))
#or
kvadrat = tall**0.5
print("Kvadratiske roten av tallet: ",  kvadrat)



# 25 Be brukeren om to ord og sjekk om de er anagrammer av hverandre.
ord1 = input("Vennligst skriv inn først ord: ").lower()
ord2 = input("Vennligst skriv inn andre ord: ").lower()

if sorted(ord1)==sorted(ord2):
    print("De er anagrammer av hverandre")
else:
    print("De er ikke anagrammer av hverandre")



# 26 Be brukeren om deres timepris og antall timer de jobbet denne uken, og beregn deres ukelønn.
timepris = float(input("Vennligst skriv inn din timepris: "))
antall_timer = float(input("Vennligst skriv inn antall timer du jobbet denne uken: "))

print("Din ukelønn: ", (timepris*antall_timer), "kroner")



# 27 La brukeren gi inn et antall sekunder og konverter dette til timer, minutter, og sekunder.
total_sekund = int(input("Vennligst skrivv in antall sekunder: "))
timer = int(total_sekund/3600)
minutter = int((total_sekund- (timer*3600))/60)
sekunder = int(total_sekund-timer*60*60-minutter*60)

print( "Etter konvertering",total_sekund, "sekunder:", timer, "timer", minutter, "minutter", sekunder, "sekunder")





# 28 Be brukeren om en pris på en vare og en rabatt i prosent, beregn den rabatterte prisen.
pris = float(input("Vennligst skriv prisen på varen: "))
rabatt = float(input("Vennligst skriv rabatt i prosent: "))
rabatterte_pris = pris*(100-rabatt)/100
print("Den rabatterte prisen:", rabatterte_pris)


# 29 Spør brukeren om et ord og skriv ut det tredje og det nest siste tegnet i ordet.
ord = input("Vennligst skriv inn et ord: ")
print(ord[2]+ord[-1])


# 30 Be brukeren om en setning og skriv ut hvert ord i setningen på en ny linje.
setning = input("Vennligst skriv inn en setning: ")
new_setning = setning.split(" ")

for i in new_setning:
    print(i)



# 31 Be brukeren om en tekst og skriv ut om teksten inneholder bokstaven 'a'.
text = input("Vennligst skriv inn en text: ")

if "a" in text:
    print("Teksten inneholder bokstaven 'a'")
else:
    print("Teksten inneholder ikke bokstaven 'a'")



# 32 Be brukeren om et tall og skriv ut tallets faktorielle.
tall = int(input("Vennligst skriv inn et tall: "))
result =1

for i in range(1, tall+1):
    result *= i
print(tall, "\b! = ", result)



# 33 Spør brukeren om en setning og skriv ut antall ord i setningen.
setning = input("Vennligst skriv inn en setning: ")
new_setning = setning.split(" ")

print("Antall ord i setningen:", len(new_setning))



# 34 Be brukeren om et ord og skriv ut ordet med store bokstaver.
ord = input("Vennligst skriv inn et ord: ").upper()
print("Ditt ord er:", ord)



# 35 La brukeren gi inn et tall og avgjøre om tallet er positivt, negativt, eller null.
tall = int(input("Vennligst skriv inn et tall: "))

if tall>0:
    print(tall, "er positivt")
elif tall<0:
    print(tall, "er negativt")
else:
    print("Tallet er zero")



# 36 Spør brukeren om tre tall og skriv ut det største tallet.
tall1 = int(input("Vennligst skriv inn tall 1: "))
tall2 = int(input("Vennligst skriv inn tall 2: "))
tall3 = int(input("Vennligst skriv inn tall 3: "))

print(max(tall1, tall2, tall3))



# 37 Be brukeren om en tekst og skriv ut antall mellomrom i teksten.
tekst = input("Vennligst skriv inn en tekst: ")
length1 = len(tekst)
removed_space = tekst.replace(" ", "")
length2=len(removed_space)
print(length1-length2)


# 38 Be brukeren om et ord, bytt ut alle vokalene med bokstaven 'x', og skriv ut det nye ordet.
ord = input("Vennligst skriv inn et ord: ")
vokal="aeiouyæøå"

for i in ord:
    if i in vokal:
        ord = ord.replace(i, "x")

print("Etter bytte ut det nye ordet:", ord)



#
# 39 Spør brukeren om et tall og skriv ut alle heltall opp til det tallet.
tall = int(input("Vennligst skriv inn et tall: "))

for i in range(1,tall+1):
    print(i)



# 40 La brukeren gi inn en setning og skriv ut setningen i omvendt rekkefølge.
setning = input("Vennligst skriv inn en setning: ")
print(setning[::-1])






