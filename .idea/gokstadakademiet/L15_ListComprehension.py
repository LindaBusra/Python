
#Example 1-opprette en liste for å få square of numbers
squared_numbers = [x**2 for x in range(1,11)]   #2^3=8, 1^2=1
print(squared_numbers)



#Example 2-lage et program, som filtrerer ut par tallene from en liste
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []
for i in numbers:
    if i%2==0:
        even_numbers.append(i)

print(even_numbers)

#or
even_numbers= [x for x in numbers if x%2==0]
print(even_numbers)



#Example 3-tall som er større enn 20
numbers = [12,21,13,45,15,16,27,28,39,10]
numbers_gerater_than_20 = [x for x in numbers if x>20]
print("numbers_gerater_than_20: ",  numbers_gerater_than_20)



#Example 4-Find prime tall (Prime tall, større enn 1, kan deles kun 1 og talen selv.)
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n% i ==0:
            return False
    return True

print(is_prime(13)) #True

prime_numbers= [x for x in range(2, 30) if is_prime(x)] [:10]
print(prime_numbers)


#å lage en liste with
text = "Gokstad akademiet!"
uppercase_letters = [letter.upper() for letter in text if letter.isalpha()]
#.isalpha() method -->den tar kun alphabetical bokstaver

print(uppercase_letters)





