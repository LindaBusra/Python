
# Loop Through a List

# Print all items in the list, one by one:
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)
    
    
print(range(len(thisList)))   # range(0,3)


# Loop Through the Index Numbers
for i in range(0,3):
        print(thisList[i])

#or
for i in range(len(thisList)):
    print(thisList[i]) 
    
print("\n------------------------------------------------------------------------------------")    
# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while(i<len(thisList)):
    print(thisList[i])
    i = i+1  
    
    
# Looping Using List Comprehension : List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thisList]
   
   
for x in ['saly', 'emily', 'john']:
    print(x)   