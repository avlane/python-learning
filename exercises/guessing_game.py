import random


LEVELS = {
    "easy": (50, 10),
    "medium": (100, 7),
    "hard": (1000, 10),
}


def play(secret, input_fn=input, output_fn=print, max_attempts=10, highest=100):
    output_fn("I am thinking of a number between 1 and {}.".format(highest))
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
    level = input("Level (easy/medium/hard)? ").strip().lower()
    highest, attempts = LEVELS.get(level, LEVELS["medium"])
    play(random.randint(1, highest), max_attempts=attempts, highest=highest)


if __name__ == "__main__":
    main()
