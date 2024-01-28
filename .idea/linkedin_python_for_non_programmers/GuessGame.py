#https://www.linkedin.com/learning/python-for-non-programmers/python-from-zero?u=171076145
import random

print("Hello")

print("Hi, Welcome to guessing game. Please guess a number between 1 and 100")
guess=int(input("What is your guess= : "))
correct_number = random.randint(1,100)
guess_count=1

while guess != correct_number:
    guess_count +=1

    if guess<correct_number:
        guess=int(input("Wrong. You need to guess higher. What is your guess?: "))
    else:
        guess=int(input("Wrong. You need to guess lower. What is your guess?: "))

print("You find the correct number in guess: ", guess_count)