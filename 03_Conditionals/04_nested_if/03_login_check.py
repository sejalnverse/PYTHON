username = input("Enter username: ")
password = input("Enter password: ")

if username == "sejal":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")