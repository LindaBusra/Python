
# def is short for define. Defining a function

def say_hello():
    print("Hello world!")

say_hello()


#Create a function called hello that prints "Hello Nick!"
def hello():
    print("Hello Nick!")
hello()


#Create a function called bark
def bark():
    print("Woof woof!")
    print("I am a dog")

bark()

#call bark() function 20 times
for x in range(20):
    bark()

print("---------------------------------------------------------------------")


#using parameter
def hello(name):
    print(f"Hello {name}!")
hello("Emily")



#using parameter
def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(3,4)



#Create a function called dog_info that takes in a dog's age and name and prints a sentence about the dog.
def dog_info(age,name):
    print(f"Hi my name is {name} and I am {age} years old")

dog_info(32,"Tomy")



#return a result infunction
def double(number):
    return number*2

print(double(5))  #or
new_number = double(5)
print(new_number)



#Create a function that returns a string in all caps
def uppercase(text):
    return text.upper()

print(uppercase("hello everyone"))



#using function in a loop
names = ['nick', 'Sara', 'emily' ]

for name in names:
    print(uppercase(name))



def add(a, b):
    return a+b;

say_hello()
print(add(3,4))



#Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)

my_function("denis", "ada")     #denis



print("---------------------------------------------------------------------")



#Ask user for enter to numbers, and find the total of them
def add(a, b):
    return a+b

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

print("total of two number: ", add(num1, num2))



