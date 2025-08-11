
# Slicing String
b = "Hello, World!"
print(b[2:5])    # llo

# Get the characters from the start to position 5 (not included):
print(b[:5])     # Hello

# Get the characters from position 5, and all the way to the end (5 included)
print(b[5:])     # , World!


# Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
b = "Hello, World!" 
print(b[-5:-2])  # orl


x = 'Welcome'
print(x[3:5])    # co
print(x[3:])     # come   