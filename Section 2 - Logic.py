#1. Basic If Statement
age = int(input(f"What is your age? "))

if age >= 18:
    print("You are an adult")

else:
    print("You are a child")

#2. If-Else Statement
import random

secret_number = random.randint(1, 10)

guess_number = int(input(f"Please guess a number between 1 and 10.  "))

if guess_number > secret_number:
    print("Too high")

elif guess_number < secret_number:
    print("Too low")

else:
    print("Correct!")

#3. If-Elif-Else Statement
score = int(input(f"What is your score (0-100)? "))

if 0 <= score < 60:
    print("F")

elif 60 <= score <=69:
    print("D")

elif 70 <= score <= 79:
    print("C")

elif 80 <= score <=89:
    print("B")

elif 90 <= score <= 100:
    print("A")

else:
    print("Invalid number. Please enter again")