
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])         # banana
print(thistuple[-1])        # cherry


# Range of Indexes
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])       # ('cherry', 'orange', 'kiwi')
print(thistuple[1:2])       # ('banana',)
print(thistuple[:4])        # ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:])        # ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[:])         # ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')


# Check if "apple" is present in the tuple:
if "apple" in thistuple:
    print("yes, 'apple' is in the fruits tuple")