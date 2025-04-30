#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)



#Use the range() and len() functions to create a suitable iterable.
for x in range(len(thistuple)):
    print(x)                        #0,1,2


for x in range(len(thistuple)):
    print(thistuple[x])             #apple, banana, cherry




#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i+=1


