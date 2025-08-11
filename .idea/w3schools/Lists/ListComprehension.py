
# The Syntax
# newlist = [expression for item in iterable if condition == True]


#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)              # ['apple', 'banana', 'mango']


#With list comprehension
newlst = [x for x in fruits if "a" in x]
print(newlst)               # ['apple', 'banana', 'mango']


#Only accept items that are not "apple":
newlst = [x for x in fruits if x != "apple"]
print(newlst)               #['banana', 'cherry', 'kiwi', 'mango']


# With no if statement:
mylist = [x for x in fruits]
print(mylist)               # ['apple', 'banana', 'cherry', 'kiwi', 'mango']


# Iterable : The iterable can be any iterable object, like a list, tuple, set etc.
mylist = [x for x in range(10)]
print(mylist)               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Accept only numbers lower than 5:
myNewList = [x for x in range(10) if x<7]       
print(myNewList)            # [0, 1, 2, 3, 4, 5, 6]


# Set the values in the new list to upper case:
myNewList = [x.upper() for x in fruits]
print(myNewList)            # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# Set all values in the new list to 'hello':
myNewList = ["Hello" for x in fruits]
print(myNewList)            # ['Hello', 'Hello', 'Hello', 'Hello', 'Hello']


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
basket = [x if x != "banana" else "orange" for x in fruits]
#if x is banana dont change it, but if it is not banaa change it with orange
print(basket)


# What will be the value of newlist?
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == "banana"]
print(newlist)      # ['banana']


# What will be the value of newlist?
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)      # ['apple', 'apple', 'apple']