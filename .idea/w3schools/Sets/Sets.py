
myset = {"apple", "banana", "cherry"}

'''
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed and do not allow duplicate values.
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
'''

thisset = {"apple", "banana", "cherry", "apple"}        # Duplicate values will be ignored:
print(thisset)

# The values True and 1 are considered the same value in sets, and are treated as duplicates
# The values False and 0 are considered the same value in sets, and are treated as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(thisset)              # {False, 'banana', 2, 'cherry', True, 'apple'}  This order can be change


print("\nGet the number of items in a set:")
print(len(thisset))


# Set Items - Data Types : Set items can be of any data type. A set can contain different data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

print("\nWhat is the data type of a set?")
print(type(set4))       # <class 'set'>


# The set() Constructor
print("\nUsing the set() constructor to make a set:")
newset = set(("apple", "banana", "cherry"))
print(newset)