#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are written with curly brackets, and have keys and values
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

#Create and print dictionary
thisCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 1980        #Duplicate values will overwrite existing values:
}

#Print the "brand" value of the dictionary:
#There is also a method called get() that will give you the same result:
print(thisCar["brand"])         #Ford
print(thisCar.get("brand"))     #Ford

#Get the value of the "model" key:
print(thisCar["year"])      #1980
print(thisCar.get("year"))

#Get the value of the "model" key:
print(thisCar["model"])



#Add new key
thisCar["owner"] = "Jack Mike"
print(thisCar)


#Dictionary Length
print(len(thisCar))         #4

#Dictionary type
print(type(thisCar))        #<class 'dict'>


#The values in dictionary items can be of any data type:
thisCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors" : ["red", "white", "blue"]
}
print(thisCar)



#It is also possible to use the dict() constructor to make a dictionary.
myDic = dict(name = "Emily", age =45, country = "Norway")
print(myDic)



#The items() method will return each item in a dictionary, as tuples in a list.
x = thisCar.items()
print("all items : ", x)        #all items :  dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('colors', ['red', 'white', 'blue'])])



#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
x = thisCar.keys()
print(x)        #dict_keys(['brand', 'model', 'year', 'colors'])




#Add a new item to the original dictionary, and see that the keys list gets updated as well:
thisCar = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors" : ["red", "white", "blue"]
}
x= thisCar.keys()
print(x)        #before the change

thisCar["color"] = "white"
print(x)



#Get Values
#The values() method will return a list of all the values in the dictionary.
y = thisCar.values()
print(y)            #dict_values(['Ford', 'Mustang', 1964, ['red', 'white', 'blue'], 'white'])



#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x= car.values()
print(x)            #dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020
print(x)            #dict_values(['Ford', 'Mustang', 2020])



print("after add  a new item to the original dictionary------------------------------")
#Add a new item to the original dictionary, and see that the values list/key list/item list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

a = car.keys()
b = car.values()
c = car.items()
#before the change
print(a)                #dict_keys(['brand', 'model', 'year'])
print(b)                #dict_values(['Ford', 'Mustang', 1964])
print(c)                #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["color"] = "red"
print(a)                #dict_keys(['brand', 'model', 'year', 'color'])
print(b)                #dict_values(['Ford', 'Mustang', 1964, 'red'])
print(c)                #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])



#Check if Key Exists
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in car:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")