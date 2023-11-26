# To print something
print("Hei")


print("This is the first line\nThis is the second line")

#use command line
wallet = 40
wallet -= 8  #I bought some food
wallet += 40

print(wallet)

#convert a text to uppercase
print('nick'.upper())


day=21
month='October'
temp=65
day_name='Tuesday'

print("Today is October 21 and it's 65 degress outside")

print("Today is" , month , day, "and it's" , temp ,"degress outside")

#f means that now you can place variables inside your string
print(f"Today is {day_name} {month} {day} and it's {temp} degress outside")



#or
age = 30
message = "My age is {}".format(age)
print(message)
print("My age is", age)


message = "Hello Norway!"
print(message[0])      # first character
print(message[0:7])    # 0 inclusive, 7 exclusive
print(len(message))    # length of text
print(message.upper()) # convert it to uppercase
print("---------------------------------------------------------------------")


x=5
y=3.14
name="Emily"
is_student=True
print(x, y, name, is_student)       #print
print(x+y)
print("Hello", name)
print("{} {} {} {}".format(x, y, name, is_student))
print("---------------------------------------------------------------------")




















