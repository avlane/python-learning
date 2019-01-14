def greeting(name):
    name = name.strip() or "world"
    return "Hello, {}!".format(name)


def main():
    print(greeting(input("What is your name? ")))


if __name__ == "__main__":
    main()
