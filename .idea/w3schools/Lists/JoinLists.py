
# Join Two Lists

# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)        # ['a', 'b', 'c', 1, 2, 3]


# use the extend() method
list3.clear()
list3.extend(list1)
list3.extend(list2)
print(list3)


# Another way to join two lists is by appending all the items from list2 into list1, one by one:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
    
print(list1)    