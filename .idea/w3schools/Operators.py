
# Python Operators

'''
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
'''
x = 9
y = 4
print(x + y)        # 13
print(x -y)         # 5
print(x * y)        # 36
print( x / y)       # 2.25  Answer is Float
print( 12 / 3)      # 4.0
print(x // y)       # 2
print(x ** y)       # 6561
print(x % y)        # 1
print("\n")


# Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)       #True
print(x is y)       #False
print(x == y )      #True
print(x is not y)   #True    
print("\n")

'''
Operator	Description	                                            Example	
is 	        Returns True if both variables are the same object	    x is y	
is not	    Returns True if both variables are not the same object	x is not y
'''


# Python Membership Operators
x= ["apple", "banana", "orange"]
print("apple" in x)         # True
print("banana" not in x)    # False
print("cherry" not in x)    # True    

'''
Operator	Description	                                                                        Example	
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
'''

# Use the correct membership operator to check if "apple" is present in the fruits object.
if "apple" in x:
    print("Yes, apple is a fruit!")
    
    
# Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
    print("5 and 10 is not equal")
    



# Python Logical Operators
'''
Operator	Description	                                                    Example	
and 	    Returns True if both statements are true	                    x < 5 and  x < 10	
or	        Returns True if one of the statements is true	                x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)
'''

# Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")
    

x = 5
print(x>3 and x<10)         # True
print(not(x>3 and x<10))    # False

  
    
    

    