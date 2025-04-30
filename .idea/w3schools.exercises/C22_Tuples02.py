# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, add items,
# and convert the list back into a tuple.


#Convert the tuple into a list to be able to change it:
x = ("banana", "apple", "cherry", "melon")
y = list(x)
y[1] = "orange"
print("My list is: ", y)
x = tuple(y)
print("My tuple is: ", x)


#add items to tuple
mytuple = ("banana", "apple", "cherry", "melon");
print("My tuple: ", mytuple)
mylist = list(mytuple)
mylist.append("orange")
mytuple =  tuple(mylist)
print("New tuple: ", mytuple)


#Add tuple to a tuple.
tuple1 = (45, 65, 76, 23)
tuple2 = (28,)      #When creating a tuple with only one item, we have to put a comma after the item
tuple1 += tuple2
print(tuple1)


#Tuples are unchangeable, so you cannot remove items from it. Because of that:
tuple1 = (45, 65, 76, 23, 67)
list1 = list(tuple1)
list1.remove(76)        #remove 76 from list
tuple1 = tuple(list1)
print(tuple1)


#0r
tuple2 = ("apple", "banana", "cherry", "orange")
list2 = list(tuple2)
list2.remove("banana")
tuple2 = tuple(list2)
print(tuple2)


#delete the tuple completely
tuple1 = (45, 65, 76, 23)
del tuple1
print(tuple1)       #NameError: name 'tuple1' is not defined




#Assign value for tuple ---> packing
fruits = ("apple", "banana", "cherry")

#extract values back into variables --> unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


#The number of variables must match the number of values in the tuple.
# If not you must use an asterisk to collect the remaining values as a list.


#Using Asterisk*
#it means, assign the rest of values as a list, in this example as alist called "red"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)      # ['cherry', 'strawberry', 'raspberry']


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)   # ['banana', 'cherry', 'strawberry']
print(red)      #
