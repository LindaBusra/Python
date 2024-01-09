#Note: All string methods return new values. They do not change the original string.

"""
Method	Description

encode()	Returns an encoded version of the string
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
splitlines()	Splits the string at line breaks and returns a list
swapcase()	Swaps cases, lower case becomes upper case and vice versa
translate()	Returns a translated string
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

#get the length of string
txt = "hello world"
print(len(txt))


#capitalize()	Converts the first character to upper case
print(txt.capitalize())


#title()	Converts the first character of each word to upper case
#istitle()	Returns True if the string follows the rules of a title
txt = "there are three spaces in this sentence"
print(txt.title())
print(txt.istitle())


#endswith()	Returns true if the string ends with the specified value
print(txt.endswith("sentence"))
print(txt.startswith("there"))


#count()	Returns the number of times a specified value occurs in a string
txt = "there are three spaces in this sentence, yes in this sentence"
print(txt.count("this"))

#replace()	Returns a string where a specified value is replaced with a specified value
txt = "Hello World"
txt = txt.replace("H", "M")

print("------------------rstrip")
#strip()	Returns a trimmed version of the string
#lstrip()	Returns a left trim version of the string
#rsplit()	Returns a right trim version of the string
txt = " Hello World "
print(txt.strip())
print(txt.lstrip())
print(txt.rstrip())


#split()	Splits the string at the specified separator, and returns a list
txt = "There are three Spaces in this sentence, Yes in this sentence"
print(txt.split(" "))



#index()	Searches the string for a specified value and returns the position of where it was found
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
print("index for 'this' is: ", txt.index("this"))           #26
print("last index for 'this' is: ", txt.rfind("this"))      #48
print("last index for 'this' is: ", txt.rindex("this"))     #48


#lower()	Converts a string into lower case
#upper()	Converts a string into upper case
#casefold()	Converts string into lower case
print(txt.upper())
print(txt.lower())
print(txt.casefold())


print("------------------------------------")
#islower()	Returns True if all characters in the string are lower case
#isupper()	Returns True if all characters in the string are upper case
print(txt.islower())
print(txt.isupper())


#isspace()	Returns True if all characters in the string are whitespaces
txt = " "
print("text consists of only whitespace characters: ", txt.isspace())       #True


#center()	Returns a centered string,
#In this example the text will be centered within a total width of 20 characters
text = "Hello everyone"
width = 20
centered_text = text.center(width)
print(centered_text)



word = input("Write a word please: ")
reverse = word[::-1]
print("Reversed word:", reverse)

