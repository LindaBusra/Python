
# Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("Print all key names in the dictionary, one by one:")
for x in thisdict:
    print(x)
    
#or    
for x in thisdict.keys():
    print(x)    
    
    
    
print("\nPrint all values in the dictionary, one by one:")  
for x in thisdict:
    print(thisdict[x])  
    
#or
for x in thisdict.values():
    print(x)    
    
    
    
print("\nLoop through both keys and values, by using the items() method:")    
for x in thisdict.items():
    print(x)
    
    
#or
for x,y in thisdict.items():
    print(x, y)    