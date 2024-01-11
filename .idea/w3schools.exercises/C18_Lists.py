
#List
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#List items are indexed, the first item has index [0], the second item has index [1] etc.


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

#or for creating list we can use list() constructor
list5 = list(("apple", "banana", False, 6))     # note the double round-brackets
print(list5)


#List Methods
"""
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""



#to find type
mylist = ["apple", "banana", "cherry", "orange"]
print(mylist)
print(type(mylist))     #<class 'list'>
print(type(list4))      #<class 'list'>


#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])



#To find length of list, use the len() function
print(len(mylist))

#Access Items
print(mylist[1])

#Negative indexing means start from the end,
# -1 refers to the last item, -2 refers to the second last item etc.
print(mylist[-1])
print(mylist[-2])


#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        #['cherry', 'orange', 'kiwi'],  2 is inclusive, 5 is exclusive
print(thislist[:4])         #starts from zero to 3
print(thislist[2:])         #from 2 to the end
print(thislist[-4:-1])      #-1 is exclusive  ['orange', 'kiwi', 'melon']


#Check if Item Exists
if "apple" in thislist:
    print("Yes, 'apple' is in the list")


#Change/replace Item Value
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist[1:3] = ["cherry", "watermelon"]
print(thislist)


#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2]=["blackcurrant", "watermelon"]
print(thislist)                                 #['apple', 'blackcurrant', 'watermelon', 'cherry']
thislist[1]=["blackcurrant", "watermelon"]
print(thislist)                                 #['apple', ['blackcurrant', 'watermelon'], 'watermelon', 'cherry']
#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist[1:3] = ["watermelon"]
print(thislist)                                 #['apple', 'watermelon', 'cherry']


#Insert Items without replacing any of the existing values
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")


#Append Items, To add an item to the end of the list, use the append() method
thislist.append("orange")
print(thislist)


#Insert item a specified index by using insert()
thislist.insert(1, "appelsin")
print(thislist)


#Extend List : To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


#Remove Specified Item
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")               #the remove() method removes the first occurance:
print(thislist)



#Remove Specified Index, The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(1)
print(thislist)
thislist.pop()          #If you do not specify the index, the pop() method removes the last item.
print(thislist)

#Remove element by using del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)


#Clear the List, The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)         # []


#copy a list
#1st way is using copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)       #['apple', 'banana', 'cherry']

#2nd way, use the built-in method list()
otherlist = list(thislist)
print(otherlist)    #['apple', 'banana', 'cherry']



#Join Two Lists
#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)        #['a', 'b', 'c', 1, 2, 3]

#or use append()
for x in list2:
    list1.append(x)
print(list1)        #['a', 'b', 'c', 1, 2, 3]

#or you can use the extend() method, it provides to add elements from one list to another list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)        #['a', 'b', 'c', 1, 2, 3]