
#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


#Loop Through the Index Numbers
for i in range(len(thislist)):
    print(thislist[i])


#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0

while i<len(thislist):
    print(thislist[i])
    i+=1


#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


print("-------------------------------------------------------------------")


#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)              #['apple', 'banana', 'mango']


#Same question:
mylist = [x for x in fruits if "a" in x]
print("mylist: ", mylist)   #['apple', 'banana', 'mango']



print("-------------------------------------------------------------------")


#The Syntax :   newlist = [expression -for- item -in- iterable -if- condition == True]


#Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = [x for x in fruits if x!="apple"]
print(new_fruits)           #['banana', 'cherry', 'kiwi', 'mango']


print("-------------------------------------------------------------------")

#You can use the range() function to create an iterable:
nwlist = [x for x in range(10)]
print(nwlist)               #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Same example, but with a condition: Accept only numbers lower than 5:
seconlist = [x for x in range(10) if x<5]
print(seconlist)            #[0, 1, 2, 3, 4]


print("-------------------------------------------------------------------")


#Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

print(newlist)              #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


#Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list2 = ["hello" for x in fruits]
print(new_list2)            #['hello', 'hello', 'hello', 'hello', 'hello']


#The Syntax :   newlist = [expression -for- item -in- iterable -if- condition == True]
#note:The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome

#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits2= [x if x!="banana" else "orange" for x in fruits ]
#If x is not "banana," it adds the same element to the newlist list. However, if x is "banana," then it adds
# the element "orange" to the newlist list.
print(fruits2)          #['apple', 'orange', 'cherry', 'kiwi', 'mango']

