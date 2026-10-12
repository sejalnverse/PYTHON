number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")

    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Number is not positive")