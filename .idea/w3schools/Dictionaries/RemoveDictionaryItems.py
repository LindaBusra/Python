
# Removing Items
# There are several methods to remove items from a dictionary

print("The pop() method removes the item with the specified key name:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)     # {'model': 'Mustang', 'year': 1964}


print("\nThe popitem() method removes the last inserted item")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)     # {'brand': 'Ford', 'model': 'Mustang'}




print("\nThe del keyword removes the item with the specified key name:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]       # {'model': 'Mustang', 'year': 1964}
print(thisdict)



print("\nThe del keyword can also delete the dictionary completely:")
del thisdict
#print(thisdict)     # NameError: name 'thisdict' is not defined



print("\nThe clear() method empties the dictionary:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)     # {}