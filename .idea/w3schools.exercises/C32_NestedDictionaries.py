#"Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries."

myfamily = {
    "child1" : {
    "name" : "Emily",
    "year" : 2000
    },
    "child2" : {
        "name" : "Mike",
        "age" : 2004
    },
    "child3" : {
        "name" : "John",
        "age" : 2010
    }
}
print(myfamily)


#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Emily",
    "year" : 2000
}
child2 = {
    "name" : "Mike",
    "age" : 2004
}
child3 = {
    "name" : "John",
    "age" : 2010
}

myfamily = {"child1" : child1,
            "child2" : child2,
            "child3" : child3}
print(myfamily)


#Access Items in Nested Dictionaries
print(myfamily["child2"])
print(myfamily["child2"]["name"])


# Python has a set of built-in methods that you can use on dictionaries.
#
# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary