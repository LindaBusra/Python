#Data Types in Python
"""
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""

#To get data type
x = 3.0
print(type(x))


#Setting Data Types
#Example                                                #Data Type
x="Hello"                                               #str
x = 20                                                  #int
x= 20.5                                                 #float
x = 1j                                                  #complex  or y= 5+6j
x = ["apple", "orange", "banana"]                       #list
x=("apple", "orange", "banana")                         #tuple      output of x is ('apple', 'orange', 'banana')
x=range(6)                                              #range  range(0,6)   6 is exclusive
x = {"name":"Mike", "age": 45}                          #dict
x = {"apple", "orange", "banana"}                       #set
x = frozenset({"apple", "orange", "banana"})            #frozenset
x = True                                                #boolean
x = b"Hello"                                            #bytes
x = bytearray(5)                                        #bytearray
x = memoryview(bytes(5))	                            #memoryview
x = None	                                            #NoneType
print(x)


#Example	                                    Data Type
x = str("Hello World")	                        #str
x = int(20)	                                    #int
x = float(20.5)	                                #float
x = complex(1j)	                                #complex
x = list(("apple", "banana", "cherry"))	        #list
x = tuple(("apple", "banana", "cherry"))	    #tuple
x = range(6)	                                #range
x = dict(name="John", age=36)	                #dict
x = set(("apple", "banana", "cherry"))	        #set
x = frozenset(("apple", "banana", "cherry"))	#frozenset
x = bool(5)	                                    #bool
x = bytes(5)	                                #bytes
x = bytearray(5)	                            #bytearray
x = memoryview(bytes(5))	                    #memoryview

x=range(6)
for i in x:
    print(i)            #0 1 2 3 4 5


