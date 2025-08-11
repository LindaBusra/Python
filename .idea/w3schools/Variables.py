x = 5
y = "John"
print(x)
print(y)


x = 4
x = "Sally"
X = "Emily"
print(x) #Sally   x and X is different, case sensitive

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
name = 'John'

print(type(x))
print(type(y))
print(type(z))
print(type(name))

# Legal variables
myvar = 'Jhon'
_myvar = 'Jhon'
myvar2 = 'Jhon'
_my_var = 'Jhon'
MYVAR = 'Jhon'
myVar = 'John'


# Illegegal variables
# 2myvar = 'Jhon'
# my var = 'Jhon'
# my-var = 'Jhon'


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


k =  l = m = 'Hello'
print(k + " " +  l + " " + m)
print(k, l, m)


#unpack a collection
fruits = ['apple', 'banana', 'cherry']
x,y,z = fruits
print(x)
print(y)
print(z)



# Output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + " " + y + " " + z)


x = 5
y = 'John'
z = 6
#print(x + y)    TypeError: unsupported operand type(s) for +: 'int' and 'st
print(x + z)
print(x, y)