
# we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age


# F-Strings
age  = 36
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price} dollars"
print(txt)


#Display the price with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)      # The price is 59.00 dollars


# A placeholder can contain Python code, like math operations:
txt = f"The price is {5 * 8} dollars"
print(txt)      # The price is 40 dollars