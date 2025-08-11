
#Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

print("Get the value of the 'model' key")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])    #or
print(thisdict.get("brand"))


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
print("\nGet a list of the keys:")
print(thisdict.keys())  # dict_keys(['brand', 'model', 'year'])


# Add new item
print("\nAdd a new item to the original dictionary, and see that the keys list gets updated as well:")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car.keys())   # before the change
car["color"] = "white"  
print(car.keys())   # after the change



# Get Values
# The values() method will return a list of all the values in the dictionary.
print("\nGet a list of the values:")
print(thisdict.values())    # dict_values(['Ford', 'Mustang', 1964])



print("\nMake a change in the original dictionary, and see that the values list gets updated as well:")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car.values())     # before the change
car["year"] = 2020
print(car.values())     # after the change



# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
print("\nGet a list of the key:value pairs")
print(thisdict.items())     # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
print("\nCheck if 'model' is present in the dictionary:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict.keys():
    print("yes1")
    
# or
if "model" in thisdict:
    print("yes2")    