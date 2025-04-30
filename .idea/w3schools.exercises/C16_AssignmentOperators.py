#Python Assignment Operators
x=15

x+=2        #x-=2   x/=3    x*=2
print(x)

x%=3        #x=x%3
print(x)

x=22
x//=3       #x=x//3
print(x)

x**=3       #x=x**3
print(x)



x = 7       # for seven : 0111   (2 system) , for tre : 0011 (2 system)
x &= 3
print(x)  # (0111 & 0011 --> 0011) -->1*2+1*1=3 (10 system)    (note:1&1=1, 1&0=0)


x = 5       #for five : 0101, for tre  (11)
x |= 3      # 0101 | 0011 -->0111  -->1*4+1*2+1*1=7   (note: 0|0=0, 1|0=1, 1|1=1)
print(x)    #7


x = 5       #for five : 101, for tre  (11)
x ^= 3      # 0101 ^ 0011 -->0110 -->1*4+1*2=6   (note: 0^0=0, 1^0=1, 1^1=0, 0^1=1)
print(x)    #6