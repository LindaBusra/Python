#Python Arrays
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

#Creating array
cars = ["Volvo", "Ford", "Hyundai", "BMW"]

print(cars)
print(cars[1])


#The Length of an Array
print(len(cars))


#Looping Array Elements
for x in cars:
    print(x)

#Adding Array Elements
cars.append("Honda")
print(cars)


#Removing Array Elements
#You can use the pop() method to remove an element from the array.
cars.pop()      #remove the last element
print(cars)
cars.pop(1)     #remove element with index 1
print(cars)

#You can also use the remove() method to remove an element from the array.
#The list's remove() method only removes the first occurrence of the specified value.
cars.remove("Hyundai")
print(cars)



# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.











