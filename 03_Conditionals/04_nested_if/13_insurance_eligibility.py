age = int(input("Enter your age: "))

if age > 0:
    if age <= 60:
        medical_status = input("Are you medically eligible? (yes/no): ").lower()

        if medical_status == "yes":
            if age <= 25:
                premium = 5000
                print("Premium category: Young adult")
            elif age <= 40:
                premium = 8000
                print("Premium category: Adult")
            else:
                premium = 12000
                print("Premium category: Mature adult")

            print(f"Annual premium: ₹{premium}")
        elif medical_status == "no":
            print("Not eligible under these practice rules")
        else:
            print("Invalid response")
    else:
        print("Age exceeds the eligibility limit")
else:
    print("Invalid age")