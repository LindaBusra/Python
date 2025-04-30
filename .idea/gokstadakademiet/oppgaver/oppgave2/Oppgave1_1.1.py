# #• Lag et program som ber brukeren om lese inn en kommaseparert linje med tall fra en fil "tall.csv"
# #og legge disse i en liste. Eksempel på fil innhold: 12, 15, 8.5, 20, 7
# import csv
#
# #lage en csv file
# file_name="tall.csv"
#
#
# #les inn tallene
# with open(file_name, "r") as file:
#     reader = csv.reader(file)       #les filen
#     string_value= next(reader)      #gå linje for linje
#     numbers = [float(value) for value in string_value]
#
# while True:
#     try:
#         deleren = float(input("Vennligst tast inn et tall kalt 'deleren': "))
#         if deleren ==0
#             raise ZeroDivisionError
#         break
#     except ValueError:
#         print("Vennligst tast inn et gyldig tall.: ")
#     except ZeroDivisionError:
#         print("Du kan ikke dele med null. Vennligst prøv igjen...")
#
# #dele hvert tall i listen med 'deleren'
# result_division = [round(sum(num / deleren, 2) for num in numbers)]
#
# #beregn gjennomsnittet av "result_division"
# average =  round(sum(result_division) / len(result_division), 2)
#
# save_to_file = input("Ønsker du å lagre resultatene til en tekstfil ('resultare.txt')? Ja/Nei")