income = float(input("Enter annual income in rupees: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
    print(f"Income tax: ₹{tax:.2f}")
elif income <= 600000:
    tax = (income - 300000) * 0.05
    print(f"Income tax: ₹{tax:.2f}")
elif income <= 1000000:
    tax = (300000 * 0.05) + ((income - 600000) * 0.10)
    print(f"Income tax: ₹{tax:.2f}")
else:
    tax = (
        (300000 * 0.05)
        + (400000 * 0.10)
        + ((income - 1000000) * 0.20)
    )
    print(f"Income tax: ₹{tax:.2f}")