
# The while Loop

print("Print i as long as i is less than 6: ")
i= 1
while i<6:
    print(i)
    i = i+1
    
    
    
# The break Statement    
print("\nExit the loop when i is 3: ")    
i=1
while i<6:
    print(i)
    if i==3:
        break
    i = i+1

    
    
# The continue Statement   
print("\nContinue to the next iteration if i is 3:")
i = 0
while i<6:
    i += 1
    if i==3:
        continue
    print(i)
    
    
# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:    
print("\nPrint a message once the condition is false:")
i=1
while i<6:
    print(i)
    i += 1
else:
    print("i is not less then 6")    
    
