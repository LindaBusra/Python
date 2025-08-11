
# Remove Specified Item: remove() method removes the first occurrence:


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)     # ['apple', 'cherry', 'banana', 'kiwi']



# Remove Specified Index: The pop() method removes the specified index.
# The del keyword also removes the specified index
thislist.pop(1)
print(thislist)     # ['apple', 'banana', 'kiwi']
del thislist[1]
print(thislist)     # ['apple', 'kiwi']
del thislist
# The del keyword can also delete the list completely.
# print(thislist)   #  name 'thislist' is not defined


# Clear the List
# The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)     # []


# What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)


