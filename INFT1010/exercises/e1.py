
print("\nExample 1-------------------------------------------------------------------------------------------------")

L = [3.6, 11.0, 5.1, 2.0, 3.0]

print(round(3.4))           # 3
print(round(3.5))           # 4
print(round(L[0]))          # 4

print(str(int(L[-1]))*3)    # 333
print(L[0] + L[1])          # 3.6+11.0=14.6
#print(L[L[-2]]**2)         # TypeError:
print(abs(-L[2]))           # 5.1
print(L[1] + int(L[3]))     # 13.0
#print(str(L[0]) + L[-3])    # TypeError: can only concatenate str (not "float") to str





print("\nExample 2-------------------------------------------------------------------------------------------------")
tallbok = {
    'NO': ['null', 'en', 'to', 'tre', 'fire', 'fem', 'seks'],
    'SE': ['noll', 'ett', 'två', 'tre', 'fyra', 'fem', 'sex'],
    'DK': ['null', 'en', 'to', 'tre', 'fire', 'fem', 'seks'],
    'IT': ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei'],
    'ES': ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis'],
    'PT': ['zero', 'um', 'dois', 'tres', 'cuatro', 'cinco', 'seis']
}

def same_word(num, tallbok):
    temp, result = {}, {}

    for landkode in tallbok:
        tallord = tallbok[landkode][num]
        if tallord in temp:
            temp[tallord].append(landkode)
            result[tallord] = temp[tallord]
        else:
            temp[tallord] = [landkode]
    return result


print(same_word(6, tallbok))