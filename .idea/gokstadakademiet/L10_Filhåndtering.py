#Filhåndtering og Arbeid med Filesystem

#Åpne en fil for lesing
with open('fil.txt', 'r') as fil:
    data = fil.read()

#Åpne en fil for skriving
# with open('ny_fil.txt', 'w') as ny_fil:
#     ny_fil.write('Dette er innholdet i den nye filen.')




# try:
#      with open('manglende_fil.txt', 'r') as fil:
#         data = fil.read()
# except FileNotFoundError:
#      print(("filen ble ikke funnet!"))


# #Arbeid med filsystem
# import os
#
# #Slett en fil
# os.remove('slett_meg.txt')
#
# #Oprett en mappe
# os.mkdir('ny_mappe')



# #Sjekk om en fil eksisterer
# if os.path.exists('fil.txt'):
#     print("Filen eksisterer.")



# #Feil håndtering og unntak
# try:
#     resultat = 10/0
# except Exception as e:
#     print(f"En feil oppstod når jeg skulle dele 10/0 : {e}")


#du kan også få enda meir informasjon i feilmeldingen vist du :
# except Exception as e:
# import traceback
# traceback.format_exc()
