
# Copy Dictionaries

print("Make a copy of a dictionary with the copy() method:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


print("\nMake a copy of a dictionary with the dict() function:")
newdict = dict(thisdict)
print(newdict)