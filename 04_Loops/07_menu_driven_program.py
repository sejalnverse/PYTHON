while True:
    print("\n1. Say Hello")
    print("2. Add two numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum =", a + b)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")