# Boolean Values

print(3<5)
print(5>1)
print(9==9)


x = 200
y = 33

if x>y:
    print("x is greater than y")
else:
    print("x is not greater than y")
    
    
# Evaluate Values and Variables
print(bool("Hello"))    
print(bool(15))
print(bool(" "))
print(bool(""))         # False
print(bool(0))          # False
print(bool(["apple", "banana"]))        # True
print(bool([]))         # False
print(bool(None))       # False


'''
Most Values are True
In fact, there are not many values that evaluate to False, 
except empty values, such as (), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False.

Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
'''
print("\n-------------------------------")



# Functions can Return a Boolean

def func():
    return 0

print(bool(func()))     # False


def func():
    return False

print(bool(func()))     # False



#-------------------------------------------------------------------------------

#Print "YES!" if the function returns True, otherwise print "NO!":
def myfunc():
    return False

if myfunc():
    print("Yes")
else:    
    print("No")    
    
    
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))       # True 

y = "Hi!"
print(isinstance(y, str))       # True