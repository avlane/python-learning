def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert(value, to):
    """Convert value to 'f' (value is Celsius) or 'c' (value is Fahrenheit)."""
    to = to.lower()
    if to == "f":
        return celsius_to_fahrenheit(value)
    if to == "c":
        return fahrenheit_to_celsius(value)
    raise ValueError("unknown unit: {!r}".format(to))


def main():
    choice = input("Convert to (F)ahrenheit or (C)elsius? ")
    try:
        value = float(input("Temperature: "))
        print(round(convert(value, choice), 1))
    except ValueError as err:
        print("Sorry:", err)


if __name__ == "__main__":
    main()
