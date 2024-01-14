#Tuples
#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#Tuples are unchangeable and ordered, meaning that we cannot change, add or remove items after the tuple has been created.
#Tuples are written with round brackets.  mytuple = ("apple", "banana", "cherry")
#Tuples allow duplicate values
#Tuple items can be of any data type


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("Emily", 40, True, "Jack", 65)

#type()
print(type(tuple4))     #<class 'tuple'>


#print a tuple:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[1])


#Print the number of items in the tuple
print("Length of tupe: ", len(thistuple))



#count()	Returns the number of times a specified value occurs in a tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
a = thistuple.count("apple")
print("count: ", a)


#index()	Searches the tuple for a specified value and returns the position of where it was found
b = thistuple.index("banana")
print("index of banana: ", b)


#Create Tuple With One Item: to create a tuple with only one item, you have to add a comma after the item
thistuple = ("apple",)
print(type(thistuple))      #<class 'tuple'>

#NOT a tuple
thistuple = ("apple")       #<class 'str'>
print(type(thistuple))

# to use the tuple() constructor for create a tuple.
thistuple = tuple(("apple", 45, False))
print(thistuple)
print(type(thistuple))


#print last item and second last item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-1])
print(thistuple[-2])

#range og indexes ( index 2 included and  index 5 not included)
print(thistuple[2:5])       #('cherry', 'orange', 'kiwi')


#By leaving out the start value, the range will start at the first item
print(thistuple[:3])        #('apple', 'banana', 'cherry')

#By leaving out the end value, the range will go on to the end of the list:
print(thistuple[3:])        #('orange', 'kiwi', 'melon', 'mango')


#Range of Negative Indexes   (index -4 included to index -1 excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])     #('orange', 'kiwi', 'melon')

#if exists:
if "apple" in thistuple:
    print("Yes, we have apple")


#Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
tuple4 = tuple1 * 3
print(tuple4)


#Print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])


#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))


#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")


#Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)



#Update () --> Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)



#Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)