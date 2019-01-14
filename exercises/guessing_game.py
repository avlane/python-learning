import random


def play(secret, max_attempts=10):
    print("I am thinking of a number between 1 and 100.")
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input("Guess {}: ".format(attempt)))
        except ValueError:
            print("Please type a whole number.")
            continue
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print("You got it in {} tries!".format(attempt))
            return True
    print("Out of tries. The number was {}.".format(secret))
    return False


def main():
    play(random.randint(1, 100))


if __name__ == "__main__":
    main()
