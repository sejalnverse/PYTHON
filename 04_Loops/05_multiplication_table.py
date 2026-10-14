number = int(input("Enter a number: "))
i = 1

while True:
    print(number, "x", i, "=", number * i)
    i = i + 1

    if i > 10:
        break