
# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.


print("Remove 'banana' by using the remove() method:")
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# !!!  If the item to remove does not exist, remove() will raise an error.
# thisset.remove("watermelon")        # KeyError: 'watermelon'


# If the item to remove does not exist, remove() will raise an error.
print("\nRemove 'banana' by using the discard() method:")
thisset.discard("watermelon)")

#You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.

print("\nRemove a random item by using the pop() method:")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()   #selects random element
print(x)
print(thisset)


print("\nThe clear() method empties the set:")
thisset.clear()
print(thisset)      #set()


print("\nThe del keyword will delete the set completely:")
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)      # NameError: name 'thisset' is not defined