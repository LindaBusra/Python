#get input from the console
user_text = input('Enter some text: ')
print(user_text.upper())


#get number from user
user_number = int(input("What do you want to double? : "))

print(user_number*2)


#or
user_number = input("What do you want to double? : ")

print( int(user_number)*2)




#First ask for some text, and then prompt "enter 1 to uppercase and 2 for lowercase: " and then either upper or lowercase it
user_text = input("Enter a text please: ")
choose = input("Enter 1 to uppercase and 2 to lowercase: ")

if choose=="1":
    print(user_text.upper())
elif choose=="2":
    print(user_text.lower())
else:
    print("You entered a invalid number")