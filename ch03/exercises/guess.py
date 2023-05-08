import random

number = int(random.randrange(1,11))
for _ in range (3):
    guess = int(input("Guess a number between 1 and 10:"))
    if guess == number:
        print("You Win!")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")