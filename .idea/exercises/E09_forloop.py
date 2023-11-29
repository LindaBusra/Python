for number in range(10):
    print("Hello")
    print(number)



fav_movies= ["Sandlot", "The Lego Movie", "Dune"]

for movie in fav_movies:
    print(movie)


#Loop 40 times and print the number of the loop times 2. Example: 2,4,6,8...

for number in range(40):
    print((number+1)*2)



#What is the sum of the numbers from 1 to 10
total = 0
for i in range(1,11):
    total += i
print("The sum is: ", total)



# for - while loop
for i in range(5):
    print(i)        # prints from 0 to 4
print("---------------------------------------------------------------------")



# for - while loop
for i in range(2,15,3): #2:start (inclusive), 15:end(exclusive)  3:avstand mellom tallene
    print(i)        # prints from 2,4,6,8,10
print("---------------------------------------------------------------------")



for i in range(1,5):
    print(i)        # prints from 1 to 4
print("---------------------------------------------------------------------")


x=5
while x>0:
    print(x)        # 5 4 3 2 1
    x-=1
print("---------------------------------------------------------------------")



#Find the numbers from 1 to 100, which are divisible by 3
for num in range(1,101):
    if num%3==0:
        print(num)
print("---------------------------------------------------------------------")



# Print 5 times Python on the console
for text in range(1,6):
    print("Python")
print("---------------------------------------------------------------------")



# What is the factoriel of 5?
s =1
for num in range(1,6):
    s *=num
    #print(s)       print all steps on the console
print("Faktoriel: ", s)





