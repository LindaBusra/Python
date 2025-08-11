x = 1
y = 35656222554887711
z = -3255522
print(type(x))          # <class 'int'>
print(type(y))          # <class 'int'>
print(type(z))          # <class 'int'>


x = 1.10
y = 1.0
z = -35.59
print(type(x))          # <class 'float'>
print(type(y))          # <class 'float'>
print(type(z))          # <class 'float'>


x = 35e3
y = 12E4
z = -87.7e100
print(type(x))          # <class 'float'>
print(x)                # 35000.0
print(type(y))          # <class 'float'>
print(y)                # 120000.0
print(type(z))          # <class 'float'>
print(z)                # -8.77e+101


x = 3+5j
y = 5j
z = -5j
print(type(x))          # <class 'complex'>
print(type(y))          # <class 'complex'>
print(type(z))          # <class 'complex'>


# Type Conversion
# You cannot convert complex numbers into another number type.!!!
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)


print(a)    #1.0
print(b)    #2
print(c)    #(1+oj)     

print(type(a))
print(type(b))
print(type(c))


#Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1,10))