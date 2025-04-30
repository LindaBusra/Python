#Once a set is created, you cannot change its items, but you can add new items.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


#To add items from another set into the current set, use the update() method.
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"pineapple", "mango", "papaya"}
fruits1.update(fruits2)
print(fruits1)


#The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
fruits1 = {"apple", "banana", "cherry"}
fruits2 = ["pineapple", "mango", "papaya"]
fruits1.update(fruits2)
print(fruits1)


#Remove "banana" by using the remove() method:
fruits1 = {"apple", "banana", "cherry"}
fruits1.remove("banana")
print(fruits1)


#Note: If the item to remove does not exist, remove() will raise an error.
fruits1 = {"apple", "banana", "cherry"}
#fruits1.remove("orange")
#print(fruits1)         #KeyError: 'orange'


#Remove "banana" by using the discard() method:
fruits1.discard("banana")
print(fruits1)


#Remove a random item by using the pop() method:
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()    #this method will remove a random item
print(x)            #The return value of the pop() method is the removed item
print(fruits)


#The clear() method empties the set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)       #set()


#The del keyword will delete the set completely:
fruits = {"apple", "banana", "cherry"}
del fruits
print(fruits)           #nothing on the console


#Loop through the set, and print the values:
fruits = {"apple", "banana", "cherry"}

for x in fruits:
    print(x)