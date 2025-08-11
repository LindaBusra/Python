print("Emily")
print('Emily')

print("She is called 'Emily'")
print('She is called "Emily"')


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)


# Strings are Arrays
a = "Hello World!"
print(a[1]) #e


for x in "banana":
    print(x)
    
    
print("The length is:", len("banana"))     # String length


# Check String
txt = "The best things in life are free!"
print("free" in txt)        #True
print("apple" not in txt)   #True

if "free" in txt:
    print("'free' is in the text")
    
print("\n")    


# Check if NOT
txt = "The best things in life are chocalade!"   
print("chocalade" not in txt) 
if "chocalade" not in txt:
    print("'chocalade' is not in the text")   
else:
    print("no, it is in the text")     

