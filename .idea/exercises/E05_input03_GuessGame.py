#Gameloop _ Number guessing game
#Our Python code will pick a random number between one and a hundred, and then ythe user will try and guess it.
#And each time that they guess we'll tell them either "you got the guess higher next time, or you gou got the get lower"
import random
import time

print("Hi! Welcome to our guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?:  "))
correct_number = 5;
random_number=random.randint(1,100)
print("Random number is : ", random_number)
count = 1

while guess != random_number:
    time.sleep(1)
    count +=1
    if guess < random_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess?:  "))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess?:  "))

print(f"Congrats! The right answer was {random_number}. It took you {count} guesses")