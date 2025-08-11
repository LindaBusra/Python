# Change Item Value
# To change the value of a specific item, refer to the index number:

thislist = ["apple", "banana", "cherry"]
thislist[1] = 'blackcurrant'
print(thislist)     # ['apple', 'blackcurrant', 'cherry']


# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)         # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']


# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)         # ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist[1:4] = ["orange"]
print(thislist)         # ['apple', 'orange']


print("What will be the result of the following syntax:")
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])            # mango
print(mylist)               # ['apple', 'kiwi', 'mango', 'cherry']


# Insert Items: The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)     # ['apple', 'banana', 'watermelon', 'cherry']


