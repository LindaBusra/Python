#and 	Returns True if both statements are true	x < 5 and  x < 10
#or	Returns True if one of the statements is true	x < 5 or x < 4
#not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


#and
x = 10
print(x>5 and x<15)

#or
x = 10
print(x>5 or x<7)

#Use the correct logical operator to check if at least one of two statements is True.


if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#not
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result


#Python Identity Operators
#is 	Returns True if both variables are the same object	x is y
#is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # returns True because z is the same object as x
print(x is y)   # returns False because x is not the same object as y
print(x == y)   # returns True, because x is equal to y

print(x is not z)   #False
print(x is not y)   #True
print(x != y)       #False


#Python Membership Operators
#in 	Returns True if a sequence with the specified value is present in the object	x in y
#not in	Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["banana", "apple"]
print("apple" in x)
print("cherry" not in x)


fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit")
