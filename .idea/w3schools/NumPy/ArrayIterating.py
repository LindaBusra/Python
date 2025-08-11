
# NumPy Array Iterating

# Iterating Arrays : Iterating means going through elements one by one.

print("Iterate on the elements of the following 1-D array:")
import numpy as np
arr =np.array([1,2,3,4,5])
for x in arr:
    print(x)
    
    
# Iterating 2-D Arrays :In a 2-D array it will go through all the rows.   
print("\nIterate on the elements of the following 2-D array:") 
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)
    
    
print("\nIterate on each scalar element of the 2-D array:")    
for x in arr:
    for y in x:
        print(y)
        
        
# Iterating 3-D Arrays : In a 3-D array it will go through all the 2-D arrays.  
print("\nIterate on the elements of the following 3-D array:")      
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
    
#To return the actual values, the scalars, we have to iterate the arrays in each dimension.    
print("\nIterate down to the scalars:")
for x in arr:
    for y in x:
        for z in y:
            print(z)
            
     
'''
Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration, lets go through it with examples.
'''        
print("\nIterate through the following 3-D array:")    
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
    
    
print("\nIterate down to the scalars with hjelp av nditer():")    
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(arr):
    print(x)