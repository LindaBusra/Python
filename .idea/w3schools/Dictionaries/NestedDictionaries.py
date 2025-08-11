
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

myFamily = {
    "child1": {
        "name" : "Emil",
        "year": 2004
    },
    
    "child2": {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3": {
        "name" : "Linus",
        "year" : 2011
    }
}


# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
    "name" : "Emil",
    "year": 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
        "name" : "Linus",
        "year" : 2011
}

myFamily = {
    "child1" :  child1,
    "child2" : child2,
    "child3" : child3
}


# Access Items in Nested Dictionaries
print(myFamily["child3"]["name"])       # Linus


# Loop Through Nested Dictionaries
print("\nLoop through the keys and values of all nested dictionaries:")
for x,obj in myFamily.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
        
        
        
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print("what will be a correct syntax for printing the name 'May'?  ")      
print(customers["c2"]["name"])      # May