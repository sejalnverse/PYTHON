attendance = float(input("Enter attendance percentage: "))

if attendance >= 75:
    fee_paid = input("Has the exam fee been paid? (yes/no): ").lower()

    if fee_paid == "yes":
        print("You are eligible for the exam")
    else:
        print("Please pay the exam fee")
else:
    print("Attendance is insufficient")