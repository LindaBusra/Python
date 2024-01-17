#Join Two Sets
#The union() method returns a new set with all items from both sets:
#Note: Both union() and update() will exclude any duplicate items.


#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)



#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)        #{'apple'}


#The intersection() method will return a new set, that only contains the items that are present in both sets.
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)            #{'google', 'microsoft', 'cherry', 'banana'}


#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)        #{2, 'cherry', 'google', 'banana'}


#copy()	Returns a copy of the set
original_set = {1, 2, 3, 4, 5}
copy_set = original_set.copy()
print(copy_set)


#Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)



#Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)



#isdisjoint()	Returns whether two sets have a intersection which is empty
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 7, 8}
print("set1 and set2 are disjoint:", set1.isdisjoint(set2))  # True  because intersection is {}
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))  # False because intersection is {3}


#issubset()	Returns whether another set contains this set or not
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6}
print(set1.issubset(set2))      #False
print(set2.issubset(set1))      #True


#issuperset()	Returns whether this set contains another set or not
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6}
print(set1.issuperset(set2))      #True
print(set2.issuperset(set1))      #False