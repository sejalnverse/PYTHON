correct_username = "sejal"
correct_password = "secure123"
correct_otp = "456789"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")

    if password == correct_password:
        otp = input("Enter verification code: ")

        if otp == correct_otp:
            print("Login successful")
        else:
            print("Incorrect verification code")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")