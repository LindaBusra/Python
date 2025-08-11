
# Looping Through a List
print("Print each fruit in a fruit list:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
    
    
# Looping Through a String    
print("\nLoop through the letters in the word 'banana':")    
word = "banana"
for x in word:
    print(x)
    
    
    
# The break Statement    
print("\nExit the loop when x is 'banana':")    
for x in fruits:
    print(x)
    if x == "banana":
        break

    
    
   
# The continue Statement    
print("\nDo not print banana:")    
for x in fruits:
    if x == "banana":
        continue
    print(x)
    
    
    
# The range() Function
print("\nUsing the range() function:")
for x in range(6):
    print(x)    
    
    
print("\nUsing the start parameter:")    
for x in range(2,6):
    print(x)  
    
    
    
# The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):  
print("\nIncrement the sequence with 3 (default is 1):")  
for x in range(2,30,3):
    print(x)
  
  
  
# Else in For Loop  
print("\nPrint all numbers from 0 to 5, and print a message when the loop has ended:")  
for x in range(6):
    print(x)
else:
    print("the number is not between 0 and 5")    
    
    
# Note: The else block will NOT be executed if the loop is stopped by a break statement. 
print("\nBreak the loop when x is 3, and see what happens with the else block:")   
for x in range(6):
    if x== 3:
        break
    print(x)
else:
    print("the number is not between 0 and 5")       
    
    
    
# Nested Loops
print("\nPrint each adjective for every fruit:")    
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
        
        
        
# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.        

print("\nExample for past statement")
for x in [0,1,2]:
    pass
    