number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    i = 1

    while i <= number:
        factorial = factorial * i
        i = i + 1

    print("Factorial:", factorial)