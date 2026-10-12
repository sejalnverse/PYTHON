amount = float(input("Enter purchase amount: "))

if amount >= 1000:
    membership = input("Do you have a membership card? (yes/no): ").lower()

    if membership == "yes":
        discount = amount * 0.10
        print(f"Discount: ₹{discount:.2f}")
        print(f"Final amount: ₹{amount - discount:.2f}")
    else:
        print("Membership required for the discount")
else:
    print("Purchase amount is too low for this discount")