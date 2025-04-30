# by Veronika Kashina


navn = input('Hva heter du?')
print(f'''Hei,{navn}! Du skal få 5 spørsmål. 
Du får 5 poenger for riktig svar og 0 hvis du svarer feil. 
Lets go!''')
print()


def quiz():
    """
    Hvis man får kun 10 poenger av 25, kan man prøve på nytt ved å svare 'ja'.

    """

    count = 0
    spm = {'spm_1': 'Hvor mange symfonier skrev Beethoven?',
           'spm_2': 'Hvilket instrument var Paganini kjent for å spille?',
           'spm_3': 'I hvilken alder døde Mozart?',
           'spm_4': '"Hvor mange musikere er det i en septett? Skriv et tall.',
           'spm_5': 'Favorittmusikkinstrumentet til Bach?'}

    svar = {'svar_1': '9',
            'svar_2': 'fiolin',
            'svar_3': '35',
            'svar_4': '7',
            'svar_5': 'orgel'}

    for i in spm:

        print(spm[i])
        answer = input()

        for j in svar:
            if answer == svar[j]:
                print(f'Gratulerer,{navn}! Du har fått 5 poenger!')
                print()
                count += 5
                del svar[j]
                break


            else:
                print(f'Beklager, det var feil svar,{navn}!')
                print()
                del svar[j]

                break
    print('Resultatene:')
    print()
    if count >= 15:
        return (f'Gratulerer,{navn}! Du har fått {count} poenger av 25! Bra jobba!')
    else:
        print(f'''Ikke så verst,{navn}, men du kan gjøre det bedre! Du har fått {count} poenger av 25.
        Skriv 'ja' hvis du ønsker å prøve å nytt.''')
    answer_2 = input().lower()
    if answer_2 == 'ja':
        print(quiz())


print(quiz())