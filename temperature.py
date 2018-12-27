choice = input("Convert to (F)ahrenheit or (C)elsius? ")
value = float(input("Temperature: "))
if choice.lower() == "f":
    print(value * 9 / 5 + 32)
else:
    print((value - 32) * 5 / 9)
