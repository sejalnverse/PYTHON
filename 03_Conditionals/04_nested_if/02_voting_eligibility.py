age = int(input("Enter your age: "))

if age >= 18:
    voter_id = input("Do you have a voter ID? (yes/no): ").lower()

    if voter_id == "yes":
        print("You meet the age and voter ID requirements")
    else:
        print("You need a voter ID")
else:
    print("You are not eligible by age")