
# Typekonvertering til int, float, bool, string

# bool() gir True for alle tall unntatt 0, 0.0
# og True for alle tekster unntatt '' (tom)
print(int('3'))
print(float(5))
print(bool(''))
print(bool("str"))
print(bool(0.0))
print(bool(0))
print(bool(5.6))
print(str(5))
print(float('4.56'))
print(int(float(5.85)))


'''
Python forstår ikke at 'fem' er et tallord
float('3,25') går ikke pga komma i stedet for punktum
int('3.25') går ikke fordi strengen har annet innhold enn et heltall, måtte brukt int(float('3.25')
'''
# Eksemplene under viser noen som ikke fungerer:
#print(int('fem'))
#print(float('3,25'))
#print(int('3.5'))


# Eksempler på behov for typekonvertering
alder = int(input("Hva er din alder?"))
print("Din dobbelt alder er: ", alder*2)        

# går ikke med string + int
#print("Jeg skal legge en heltall to string " + 5 )      # TypeError: can only concatenate str (not "int") to str
print("Jeg skal legge en heltall to string " + str(5) )
tall =3.25
print("Jeg skal legge en heltall to string", f"{5}")
print("Jeg skal legge en heltall to string", f"{tall}")



# Annen løsning for konvertering til streng: f-string
def myfunc(navn, alder):
    print(f"ditt navn er {navn} og din alder er {alder}")
    
myfunc("emily", 25)    

def land_info(navn, areal, folketall, hovedstad):
    return f'{navn},\t {areal} km2,\t {folketall:.2f} mill.\t {hovedstad}'

print(land_info('Norge', 323781, 5.391, 'Oslo'))
print(land_info('Sverige', 447375, 10.729, 'Stockholm'))
print(land_info('Canada', 9984670, 38.6547, 'Ottawa'))