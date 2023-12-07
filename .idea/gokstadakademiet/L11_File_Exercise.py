
#åpne og lese fra og skrive til fil

# with open('tekstfil.txt', 'r') as fil:
#     innhold = fil.read()
#     print(innhold)



#lage en ny fil
# with open('ny_fil.txt', 'w') as fil:
#     fil.write("Dette er en ny fil")


#Open the file with write ('w') permission
with open("New_file.txt", 'w') as file:
    #write text to the file
    file.write("Hello World! ")


#å lese innholdet fra en linje og lese linje og linje
# with open("ny_fil.txt", 'r') as fil:
#     for linje in fil:
#         print(linje)



#find eksisterende fil, åpne den, å legge flere text
# with open("ny_fil.txt", 'a') as fil:
#     fil.write("Dette er ekstra text")


