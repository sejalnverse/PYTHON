while True:
    print("\n--- MENU ---")
    print("1. Say Hello")
    print("2. Add two numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Sum:", num1 + num2)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")