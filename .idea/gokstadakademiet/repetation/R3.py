# Oppgave 6
befolkning = {"Oslo":680000, "Kristiansand" : 200000, "Trondheim" : 158000 }

by =input("Skriv inn en by: ").title()
if by in befolkning:
    print(f"Befolkningen i {by} er : {befolkning[by]} ")
else:
    print(f"Fant ikke informasjon on  {by}")



# Oppgave 8
for num in range(2,51):
    if num == 23:
        continue
    for i in range(2, num):
        if num%i == 0:
            break
    else:
        print(num)