import random

secret = random.randint(1, 100)
tries = 0
print("I am thinking of a number between 1 and 100. You have 10 tries.")
while tries < 10:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("You got it in", tries, "tries!")
        break
else:
    print("Out of tries. The number was", secret)
