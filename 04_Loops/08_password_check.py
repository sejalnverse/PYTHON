correct_password = "python123"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    print("Incorrect password. Try again.")