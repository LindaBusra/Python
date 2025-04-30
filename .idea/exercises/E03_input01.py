# Ask user name
name =input("What is your name: ")
print("Hello, ", name)



#Ask user for enter to numbers, and find the total of them
def add(a, b):
    return a+b

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

print("total of two number: ", add(num1, num2))



# if-else with input
alder = int(input("Skriv inn din alder:"))

if alder<18:
    print("Du er ikke myndig!")
else:
    print("Du er mynding!")



#Find the number is prime or not
number = int(input("Enter a number please: "))

count=0
for i in range(1, number+1):
    if number%i == 0:
        count +=1

if count==2:
    print("The number is prime")
else:
    print("The number is not prime")