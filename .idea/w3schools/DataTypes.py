"""   
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType 
"""


# Getting data type
x= 5
y = 'Hello'
z = 1j
k = 20.5
a = ['apple', 'banana', 'orange']
b = ('apple', 'banana', 'orange')
c = range(6)
d = {'name':'John', 'lastname':"Nilsen"}
e = {'John', "Emily", "James"}
m = True
print(type(x))      #int
print(type(y))      #str
print(type(z))      #complex
print(type(k))      #float
print(type(a))      #list
print(type(b))      #tuple

print(c)            #range(0, 6)
print(type(c))      #range
print(type(d))      #dict
print(type(e))      #set
print(type(m))      #bool




myvar = list(("banana", "orange", "cherry"))    
print(myvar)            # ['banana', 'orange', 'cherry']
print(type(myvar))      # <class 'list'>   


myvar = tuple(("banana", "orange", "cherry"))    
print(myvar)            # ('banana', 'orange', 'cherry')
print(type(myvar))      # <class 'tuple'>   


myvar = set(("banana", "orange", "cherry"))    
print(myvar)            # {'banana', 'orange', 'cherry'}
print(type(myvar))      # <class 'set'>   


myvar = dict(name='Emily', age=36)   
print(myvar)            # {'name': 'Emily', 'age': 36}
print(type(myvar))      # <class 'dict'>   

myvar = range(8)
print(myvar)            # range(0, 8)
print(type(myvar))      # <class 'range'>


myvar = bool(7)
print(myvar)            # True
print(type(myvar))      # <class 'bool>



