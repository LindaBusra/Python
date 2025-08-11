# Loop Through a Tuple

print("print tuple items:")
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
    
# Loop Through the Index Numbers    
print("\nPrint all items by referring to their index number:")
for i in range(len(thistuple)):
    print(thistuple[i])
    
    
# Using a While Loop    
print("\nPrint all items, using a while loop to go through all the index numbers:")
i = 0
while(i<len(thistuple)):
    print(thistuple[i])
    i += 1