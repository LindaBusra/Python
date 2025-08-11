# Change Values
# You can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2024
print(thisdict)


# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({"year" : 2025})
print(thisdict)


x = {'type' : 'fruit', 'name' : 'banana'}
print("\nWhat is a correct syntax for changing the name from banana to apple?")
x["name"] = "apple"
print(x)

#or
x.update({"name" : "cheery"})
print(x)



x = {'type' : 'fruit', 'name' : 'banana'}
print("\nWhat is a correct syntax for changing the type from fruit to berry?")
x["type"] = "berry"
print(x)