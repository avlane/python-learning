import random


def play(secret, input_fn=input, output_fn=print, max_attempts=10):
    output_fn("I am thinking of a number between 1 and 100.")
    attempt = 0
    while attempt < max_attempts:
        try:
            guess = int(input_fn("Guess {}: ".format(attempt + 1)))
        except ValueError:
            # typos should not cost an attempt
            output_fn("Please type a whole number.")
            continue
        attempt += 1
        if guess < secret:
            output_fn("Too low")
        elif guess > secret:
            output_fn("Too high")
        else:
            output_fn("You got it in {} tries!".format(attempt))
            return True
    output_fn("Out of tries. The number was {}.".format(secret))
    return False


def main():
    play(random.randint(1, 100))


if __name__ == "__main__":
    main()
