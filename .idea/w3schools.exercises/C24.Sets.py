
#To store collection of data : List, Set, Tuple, Dictionary


#Sets are used to store multiple items in a single variable.
#Set items are unchangeable, Once a set is created, you cannot change its items, but you can remove items and add new items.
#Sets are written with curly brackets.
#Set items are unordered, unchangeable, and do not allow duplicate values.


#Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)


#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


#Get the number of items in a set:
print(len(thisset))

#Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1,6,9,2}
set3 = {False, True, False}
set4 = {"apple", 5, False, 55}


#type of set
print(type(set4))       #<class 'set'>


#Using the set() constructor to make a set:
myset = set(("apple", 3, 5))        ## note the double round-brackets
print(myset)


#Loop through the set, and print the values:
fruits = {"apple", "banana", "cherry"}
for x in fruits:
    print(x)


#Check if "banana" is present in the set:
print("banana" in fruits)       #True