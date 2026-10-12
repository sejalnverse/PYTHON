correct_pin = "1234"
balance = 10000

pin = input("Enter your ATM PIN: ")

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: "))

    if amount > 0:
        if amount % 100 == 0:
            if amount <= balance:
                balance = balance - amount
                print("Withdrawal successful")
                print(f"Remaining balance: ₹{balance:.2f}")
            else:
                print("Insufficient balance")
        else:
            print("Withdrawal must be a multiple of ₹100")
    else:
        print("Invalid withdrawal amount")
else:
    print("Incorrect PIN")