
# Append Items 


# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)                                 # ['apple', 'banana', 'cherry', 'orange']

# To insert a list item at a specified index, use the insert() method.
thislist.insert(1, "watermelon")               
print(thislist)              # ['apple', 'watermelon', 'banana', 'cherry', 'orange']


# To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)             # ['apple', 'watermelon', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya']


# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thistuple = ("kiwi", "peer")
thislist.extend(thistuple)
print(thislist)             # ['apple', 'watermelon', 'banana', 'cherry', 'orange', 'mango', 'pineapple', 'papaya', 'kiwi', 'peer']


tropical = ["mango", "pineapple", "papaya"]
handle  = ["kiwi", "banana"]
tropical.insert(1, handle)
print(tropical)


#What will be the result of the following syntax:
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])   # apple