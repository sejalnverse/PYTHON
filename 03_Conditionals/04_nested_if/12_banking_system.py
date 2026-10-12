correct_pin = "5678"
balance = 25000.0

pin = input("Enter your PIN: ")

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: "))

    if amount > 0:
        if amount % 100 == 0:
            if amount <= balance:
                balance -= amount
                print("Transaction successful")
                print(f"Remaining balance: ₹{balance:.2f}")
            else:
                print("Insufficient balance")
        else:
            print("Amount must be a multiple of ₹100")
    else:
        print("Withdrawal amount must be positive")
else:
    print("Incorrect PIN")