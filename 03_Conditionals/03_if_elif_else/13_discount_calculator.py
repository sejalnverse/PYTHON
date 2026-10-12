amount = float(input("Enter purchase amount in rupees: "))

if amount < 0:
    print("Invalid purchase amount")
elif amount < 1000:
    discount_rate = 0
elif amount < 5000:
    discount_rate = 0.05
elif amount < 10000:
    discount_rate = 0.10
else:
    discount_rate = 0.20

if amount >= 0:
    discount = amount * discount_rate
    final_amount = amount - discount

    print(f"Discount: ₹{discount:.2f}")
    print(f"Final amount: ₹{final_amount:.2f}")