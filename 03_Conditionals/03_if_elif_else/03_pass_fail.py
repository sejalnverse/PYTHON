marks = float(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 75:
    print("Distinction")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")