login = input("Are you logged in? (yes/no): ").lower()

if login == "yes":
    registration = input("Are you registered for the exam? (yes/no): ").lower()

    if registration == "yes":
        attendance = float(input("Enter attendance percentage: "))

        if 0 <= attendance <= 100:
            if attendance >= 75:
                exam_available = input("Is the exam available now? (yes/no): ").lower()

                if exam_available == "yes":
                    print("You may start the exam")
                elif exam_available == "no":
                    print("The exam is not available yet")
                else:
                    print("Invalid response")
            else:
                print("Attendance requirement not met")
        else:
            print("Invalid attendance percentage")
    elif registration == "no":
        print("You must register first")
    else:
        print("Invalid registration response")
elif login == "no":
    print("Please log in first")
else:
    print("Invalid login response")