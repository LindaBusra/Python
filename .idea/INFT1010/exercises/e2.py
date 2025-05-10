import numpy as np
n=2
x=3.0
s='Python'
t=[1,2,'tre']

# print(t*x)  error
print(n%5)      #2
print(t[-1])    #tre

print(n*x)      #float
#print(s[x])     #error
print(8/n)      #float
#print(t+n)     #can only concatenate list (not "int") to list
print(t*n)      #list

print("-----------------------------------------------------------------")
def fu(txt, x):
    i = 0
    for j in range(len(txt)):
        if txt[j].isdigit():  # Eğer karakter bir rakamsa, döngü devam eder
            continue
        
        try:
            # txt[i:j] aralığındaki kısmı integera dönüştürmeye çalışıyoruz
            d = int(txt[i:j])
        except ValueError:
            # Eğer dönüştürülemezse varsayılan değer 1 olur
            d = 1
        
        # 'r' karakterine göre x'in değeri artırılıyor
        if txt[j] == 'r':
            x += d
        # 'l' karakterine göre x'in değeri azaltılıyor
        if txt[j] == 'l':
            x -= d
        
        # i'yi j'nin bir fazlasına ayarlıyoruz
        i = j + 1
    
    # x değerini döndürüyoruz
    return x


print(fu("", 0))
print(fu("2r3l",0))
#print(fu("lr")) error
print(fu("12",0))
print(fu("hello", 0))
print(fu("3l 2r", 1))