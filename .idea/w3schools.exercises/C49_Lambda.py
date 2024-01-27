#A lambda function can take any number of arguments, but can only have one expression.

#Syntax
#lambda arguements: expression


#Example-1: #Add 10 to argument a, and return the result:
x = lambda a : a+10
print(x(10))


#Example-2: #Multiply argument a with argument b and return the result:
y = lambda a,b : a * b
print(y(5,3))

#Example-3:
z = lambda a,b,c : a+b+c
print(z(4,5,6))


#Example-3: Make a function that always doubles the number you send in:
def myfunction(n):
    return lambda a : a*n

mydoubler = myfunction(2)
print(mydoubler(10))


#Example-4: Use the same function definition to make a function that always triples the number you send in
mytripler = myfunction(3)
print(mytripler(40))


#Create a lambda function that takes one parameter (a) and returns it.
c = lambda a : a
print(c(5))