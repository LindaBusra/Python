
'''
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
Since tuples are indexed, they can have items with the same value:
'''

mytuple = ("apple", "banana", "cherry")
print(mytuple)          # ('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))   # 5


# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

newtuple = ("apple",)       
print(newtuple)             # ('apple',)
print(type(newtuple))       # <class 'tuple'>

newtuple = ("apple")
print(newtuple)             # apple    Not a tuple
print(type(newtuple))       # <class 'str'>


# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")


# The tuple() Constructor
thistuple = tuple(("saly", "adam", "mike", "jeny"))     # note the double round-brackets
print(thistuple)