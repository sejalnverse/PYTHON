number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    print("Factors:")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)