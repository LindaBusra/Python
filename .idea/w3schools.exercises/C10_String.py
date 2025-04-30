
a = "Hello World"


print(a[0])         #prints frist character
print(len(a))       #prints the length of the string
print(a[2:5])       #Get the characters from index 2 to index 4
print(a[:5])        #Get the characters from index start to index 4
print(a[2:])        #Get the characters from index 2 to end


print(a[-5:-2])     #orl, Use negative indexes to start the slice from the end of the string
#"o' is in "World!" in position -5.  d is in position -2, in "World!" but not included



txt = " Hello World "
print(txt.strip())  #Return the string without any whitespace at the beginning or the end
print(txt.upper())  #Convert the value of txt to upper case.
print(txt.lower())  #Convert the value of txt to lower case.

txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)


#Split String
txt = "Hello, My Litle World"
print(txt.split(","))       #['Hello', ' My Litle World']


#loop for string
for x in "banana":
    print(x)

#sort()
text = "Hello"
print("after sort method: ", sorted(text))


#Check String : To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "Like many other popular programming languages, " \
      "strings in Python are arrays of bytes representing unicode characters."
print("Python" in txt)  #True


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is in the text")




#Check if NOT
#To check if a word or character is NOT in a string, we can use "not in"
print("free" not in txt)    #False



if "free" not in txt:
    print("The life is not good")
else:
    print("The life is good")

