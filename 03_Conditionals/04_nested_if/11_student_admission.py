marks = float(input("Enter academic marks percentage: "))

if 0 <= marks <= 100:
    if marks >= 60:
        entrance_score = float(input("Enter entrance exam score (0-100): "))

        if 0 <= entrance_score <= 100:
            if entrance_score >= 70:
                seats_available = input("Are seats available? (yes/no): ").lower()

                if seats_available == "yes":
                    print("Admission confirmed")
                elif seats_available == "no":
                    print("No seats available")
                else:
                    print("Invalid response")
            else:
                print("Entrance score is insufficient")
        else:
            print("Invalid entrance score")
    else:
        print("Academic marks are insufficient")
else:
    print("Invalid academic marks")