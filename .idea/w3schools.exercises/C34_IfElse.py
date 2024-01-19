# Python Conditions and If statements

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#Example:
a = 330
b = 200
if a>b:
    print("a is greater than b")


#Elif : The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 330
b = 200
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")


#Else : The else keyword catches anything which isn't caught by the preceding conditions.
#You can also have an else without the elif
a = 130
b = 200
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")




#Short Hand If
#This technique is known as Ternary Operators, or Conditional Expressions.
#If you have only one statement to execute, you can put it on the same line as the if statement.
a = 230
b = 200
if a>b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a>b else print("B")


#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a>b else print("=") if a==b else print("B")


#AND  #OR
a = 550
b = 33
c = 500

if a>b and a>c:
    print("Both conditions are True")

if a>b or a>c:
    print("At least one of the conditions is True")


#NOT
a = 33
b = 200
if not a>b:
    print("a is NOT greater than b")


#Nested If
#You can have if statements inside if statements, this is called nested if statements.
x=45

if x>20:
    print("Above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20!")


#The pass Statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 20
b = 150

if a<b:
    pass
else:
    print("a")