
'''
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets.
List Items : are ordered, changeable, and allow duplicate values. 
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value
'''



myList = ["apple", "banana", "cherry", "apple"]
print(myList)           # ['apple', 'banana', 'cherry', 'apple']
print(type(myList))     # <class 'list'>

# List Length
print(len(myList))  # 4

# List items can be of any data type. A list can contain strings, integers and boolean values.
list1 = [1, 2, 3]
list2 = ["apple", "banana", "cherry"]
list3 = [True, False]
list4 = [True, 2, "apple", 40]


# Using list() constructor when creating a new list.
thislist = list(("apple", "banana"))        # note the double round-brackets
print(thislist)                             # ['apple', 'banana']


# Remove item from list 
thislist.remove("apple")
print(thislist) 



mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])        #mango