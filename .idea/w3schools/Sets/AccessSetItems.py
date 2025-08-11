
# Access Items
print("\nLoop through the set, and print the values:")
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    

print("\nCheck if 'banana' is present in the set:")    
for x in thisset:
    if x=="banana":
        print("yes it is in the set")

#0r
print("banana" in thisset)


print("\nCheck if 'banana' is NOT present in the set:")
print("banana" not in thisset)


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.