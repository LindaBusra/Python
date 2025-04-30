#Loop Through a Dictionary

#Example-1 Print all key names in the dictionary, one by one:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1996
}
for x in car:
    print(x)

#You can use the keys() method to return the keys of a dictionary:
for x in car.keys():
    print(x)




#Example 2- Print all values in the dictionary, one by one:
for x in car:
    print(car[x])

#You can also use the values() method to return values of a dictionary:
for x in car.values():
    print(x)


#Example 3-Loop through both keys and values, by using the items() method:
for x,y in car.items():
    print(x,y)




#Copy a Dictionary
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1996
}
new_car = car.copy()
print("Cretae new_car with copy() method: ", new_car)


#Another way to make a copy is to use the built-in function dict().
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1996
}
new_car = dict(car)
print("Cretae new_car with dict() method: ", new_car)