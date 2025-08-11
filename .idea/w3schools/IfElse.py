
'''Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''


a = 38
b = 33
if b>a:
    print("b is greater than a")
elif b==a:
    print("b is equals a")    
else:
    print("b is less than a")    
    
    
# Short Hand If
print("\nOne line if statement:")
if a>b : print("a is greater than b")
    
# Short Hand If ... Else
print("\nOne line if else statement:")
print("A") if a>b else print("B")    


print("\nOne line if else statement, with 3 conditions:")
a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")


# And
print("\nTest if a is greater than b, AND if c is greater than a:")
a = 200
b = 33
c = 500
if a>b and c>a:
    print("Both conditions are ture")
    
    
# Or
print("\nTest if a is greater than b, OR if a is greater than c:")    
if a>b or a>c:
    print("At least one of the conditions is true")
    
   
# Not
print("\nTest if a is NOT greater than b:")
a = 33
b = 200
if not a>b:
    print("a is not greater than b")
    
    
# Nested If
print("\nYou can have if statements inside if statements, this is called nested if statements.")    
x = 41
if x>10:
    print("above ten")
    if(x>20):
        print("and also above 20")
    else:
        print("but not above 20")    
   
    
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.    
a = 33
b = 200

if b>a:
    pass


