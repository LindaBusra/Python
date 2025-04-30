import random


number = random.randint(1,10) #give me number between 1 and 10

print(number)

print(random.random()) #it gives number between 0 and 1  like 0.49048398627251




#make your own version of a magic 8 ball that prints yes, no or maybe each time you ask it

answer =random.randint(1,3)
if answer==1:
    print("Yes")
if answer==2:
    print("No")
if answer==3:
    print("Maybe")



#Lucky Number game
import random

lucky_number= random.randint(1,100)
fortune_number=random.randint(1,3)
fortune_text= ""

#Choosing what fortune to show

if fortune_number ==1:
    fortune_text = 'You will have a great day'
if fortune_number ==2:
    fortune_text = 'Today will be tough...but worth it'
if fortune_number ==3:
    fortune_text = 'You will get married this year'

print(f"{fortune_text} Your Lucky Number is: {lucky_number} ")
