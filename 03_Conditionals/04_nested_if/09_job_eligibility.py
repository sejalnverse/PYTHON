age = int(input("Enter your age: "))

if age >= 18:
    qualification = input("Do you have the required qualification? (yes/no): ").lower()

    if qualification == "yes":
        experience = float(input("Enter years of experience: "))

        if experience >= 0:
            if experience >= 1:
                print("You meet the age, qualification, and experience requirements")
            else:
                print("You meet the age and qualification requirements but lack experience")
        else:
            print("Invalid experience")
    elif qualification == "no":
        print("Required qualification is missing")
    else:
        print("Invalid qualification response")
else:
    print("You do not meet the minimum age requirement")