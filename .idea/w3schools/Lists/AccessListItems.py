# Access Items
# List items are indexed and you can access them by referring to the index number:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0])


# Negative Indexing : It starts from the end. -1 refers to the last item, -2 refers to the second last item etc.
print(thislist[-1])     # mango


#Range of Indexes
print(thislist[2:5])    # ['cherry', 'orange', 'kiwi']
print(thislist[:4])     # ['apple', 'banana', 'cherry', 'orange']  (4 is not include)
print(thislist[2:])     # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[-4:-1])  # ['orange', 'kiwi', 'melon']   This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)


# Check if Item Exists
if "apple" in thislist:
    print("yes, 'apple' is in the list")
 

