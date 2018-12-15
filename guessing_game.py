import random

secret = random.randint(1, 100)
guess = 0
print("I am thinking of a number between 1 and 100.")
while guess != secret:
    guess = int(input("Your guess: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
print("You got it!")
