
# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

fruits = ("apple", "banana", "cherry")
print(fruits)

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
    
    
# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.    

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)        # apple
print(yellow)       # banana
print(red)          # ['cherry', 'strawberry', 'raspberry']
print("\n")    


# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)        # apple
print(tropic)       # ['mango', 'papaya', 'pineapple']
print(red)          # cherry