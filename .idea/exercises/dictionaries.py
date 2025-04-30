#Dictionaries -> key-value pairs
cats = {"Jane":6, "Tom":14, "Sara":8}
print(cats)
print(cats["Tom"]) #get the value

#add an item
cats["Wilson"] = 1
print(cats)

#delete an item
del(cats["Tom"])
print(cats)

#length of dictionary
print(len(cats))



#Create a dictionary with Ints for keys and Booleans for values
ints_and_bools = {1:True, 2:False,3:False}
