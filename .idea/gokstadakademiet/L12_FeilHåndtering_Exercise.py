
#Håndtere FileNotFoundError
# try:
#     with open("manglende_fil.txt", 'r') as fil:
#         innhold = fil.read()
#         print(innhold)
# except FileNotFoundError:
#     print("Filen ble ikke funnet")



#åpne fil uten riktig tillatelse, for PermissinErrors
# try:
#     with open('/root/forbudt.txt','w') as fil:
#         fil.write("Dette er forbudt")
# except PermissionError:
#     print("Du har ikke tillatelse til å skrive til denne filen")




input_fra_kunde=0
input_fra_office="200"


#Handtere unntak
# try:
#     resultat = input_fra_office/input_fra_kunde
#
# except ZeroDivisionError:
#     print("Du kan ikke dele på null")
# except Exception as e:
#     print(f"En feill oppstod: {e}")





