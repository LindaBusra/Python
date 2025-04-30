
#with lambda funksjon
multiply = lambda x,y :  x*y
print(multiply(3,4))


#with funksjon
def multiply(x, y):
    resultat = x*y
    return resultat
print(multiply(3,4))


#lage en funksjon som sorterer text basert på lengen
strings=["strawberry", "apple", "banana", "cherry", "melon"]
sorted_strings = sorted(strings)
print(sorted_strings)
sorted_strings_with_length = sorted(strings, key=lambda x:len(x))
#reverse:default is false
print(sorted_strings_with_length)
sorted_strings_with_length = sorted(strings, key=lambda x:len(x), reverse=True)
print(sorted_strings_with_length)



#med lambda
classify_number = lambda x: "Positive" if x>0 else "Negative"
result = classify_number(-5)
print(result)


#med å bruke funksjon
def classify_number(x):
    if x>0:
        return "Positive"
    else:
        return "Negative"
result = classify_number(-5)

print(result)



#filtrere elementer fra liste
numbers = [-3, -5, -1, 5, 8, -2, 10]
positive_numbers = list(filter(lambda  x: x>0, numbers))
print(positive_numbers)



#converter  celsius til fahrenheit
celsius_temperatures = [0,10,20,30,40]
fahrenheit_temperatures = list(map(lambda x: (x*9/5) +32, celsius_temperatures))
print(fahrenheit_temperatures)
