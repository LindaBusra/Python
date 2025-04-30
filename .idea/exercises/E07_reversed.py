#reverse of text

#1.way
text = input("Enter the first text: ")
reversed_text = text[::-1]
print("Reversed text : ", reversed_text)


#2.way
text = input("Enter the second text: ")
reversed_text = "".join(reversed(text))
print("Reversed text : ", reversed_text)


#3.way
text = input("Enter the third text: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed text : ", reversed_text)


# Is it palindrome
text = input("Enter a text please: ")
reversed_text = "".join(reversed(text))

if text == reversed_text:
    print("The given text is palindrome")
else:
    print("The given text is not palindrome")

