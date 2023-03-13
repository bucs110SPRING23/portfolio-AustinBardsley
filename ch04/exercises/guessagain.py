import random

number = int(random.randrange(1,1000))
guesses = 0
guess = []
while guess != number:
    guess = int(input("Guess a number between 1 and 1000:"))
    if guess > number:
        print("Too High")
    elif guess<number:
        print("Too Low")
    guesses += 1
print("You Win!")
print("You took", guesses , "guesses")