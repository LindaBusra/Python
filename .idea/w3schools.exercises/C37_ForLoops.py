# Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)


# Exit the loop when x is "banana":
print("\nusing break in for loop...")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break


# Exit the loop when x is "banana", but this time the break comes before the print:
print("\nusing break in for loop...")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break
    print(x)


#Continue
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print "banana"
print("\nusing Continue in for loop...")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)


#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)    #starts from 0, and increment by 1, 6 is exclusive


for x in range(2,7):
    print(x)


#the increment value by adding a third parameter:
for x in range(3,14,3):
    print(x)


#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished")


# The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x==3: break
    print(x)
else:
        print("Finally finished")


# Nested Loops: A nested loop is a loop inside a loop."

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)


#The pass Statement
#for loops cannot be empty, but if you for some reason have a for loop with no content,
#put in the pass statement to avoid getting an error.

for x in[0,1,2]:
    pass
# having an empty for loop like this, would raise an error without the pass statement
