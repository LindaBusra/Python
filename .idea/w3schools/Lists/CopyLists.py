
# copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


# Another way to make a copy is to use the built-in method list()
thislist = ["saly", "emily", "john"]
names = list(thislist)
print(names)


# You can also make a copy of a list by using the : (slice) operator.
thislist = ["saly", "emily", "john", "mike", "amalie"]
names = thislist[:]
print(names)