marks = float(input("Enter your marks percentage: "))

if 0 <= marks <= 100:
    if marks >= 80:
        income = float(input("Enter annual family income: "))

        if income >= 0:
            if income < 300000:
                print("You are eligible for the scholarship")
            else:
                print("Family income exceeds the scholarship limit")
        else:
            print("Invalid income")
    else:
        print("Marks are insufficient for the scholarship")
else:
    print("Invalid marks")