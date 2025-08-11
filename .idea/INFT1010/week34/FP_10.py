
# Datatyper i Python: int, float, bool, string

#Heltall (int)
antall = 15
a = antall**2
print(a)

#Float
radius = 2.4
omkrets = radius * 3.14
NA = 6.02214076e23
kB = 1.380649e-23
print(NA * kB)


#bool
ok = True
funnet = False
a = 3
b = 4
er_like = 3==4
print(er_like)      #False
print( 0 == 0.0)    # True


# string
univ = "NTNU"
by = "Trondheim"
print(univ[0])      # N
print(by[-1])       # m    negativ indeks teller bakfra
#print(univ[0.0])    # index må være helttalll


# Type
print(type(a))
print(type(funnet))
print(type(univ))
print(type(NA))


print("\n-----------------------------------------------------------------")
i1 =15
i2 =5
f2 = 5.0
boolElement = True
print(i1+i2)
print(i1+f2)                # resultat blir float hvis minst en operand er float
print(i1 * boolElement)     # 15
print(i1/i2)                # 3.0    int / int blir også float
print(i1//i2)               # 3
print(i1*i2, "apple"*i2)    # 75 appleappleappleappleapple


s1 = "51"
s2 = "50"
print(s1 + s2)  #5150
print(s1 * 3)   #515151     #en tekststreng kan "ganges" med et heltall
#print(s1 * 3.0)