#Change Values: You can change the value of a specific item by referring to its key name:

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

car["year"] = 1970
print(car)


#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
car.update({"year":2020})
print(car)


#Adding Items
#The argument must be a dictionary, or an iterable object with key:value pairs.
car.update({"color" : "red"})
print(car)


#Adding Items
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
car["color"] = "red"
print(car)




#Removing Items
#1- The pop() method removes the item with the specified key name:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
car.pop("model")
print(car)


#2-The popitem() method removes the last inserted item
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
car.popitem()
print(car)


#3-The del keyword removes the item with the specified key name:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del car["model"]
print(car)



#4-The clear() method empties the dictionary:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
car.clear()
print("after clean() method: ", car)



#5- The del keyword can also delete the dictionary completely:
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del car
#print(car)      #NameError: name 'car' is not defined.
