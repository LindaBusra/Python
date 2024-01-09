
#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#or
print(f"My name is John, and I am {age}")

#or
print("My name is John, and I am", age)


#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
#Example
quantity = 3
item_no = 200
price =50.25
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no,price ))


#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
your_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity, item_no,price ))