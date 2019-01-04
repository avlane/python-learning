choice = input("Convert to (F)ahrenheit or (C)elsius? ")
try:
    value = float(input("Temperature: "))
except ValueError:
    print("That is not a number.")
else:
    if choice.lower() == "f":
        print(value * 9 / 5 + 32)
    else:
        print((value - 32) * 5 / 9)
