
# Python Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.get("brand"))

print("\nDuplicate values will overwrite existing values:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))       # <class 'dict'>

# Dictionary Items - Data Types :The values in dictionary items can be of any data type:
print("\nString, int, boolean, and list data types:")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "blue", "white"]
}


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
print("\nUsing the dict() method to make a dictionary:")
mydict = dict(name="John", age=36, country="Norway")
print(mydict)

