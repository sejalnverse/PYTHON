weight = float(input("Enter parcel weight in kg: "))

if weight <= 0:
    print("Invalid weight")
elif weight <= 1:
    shipping_cost = 50
    print(f"Shipping cost: ₹{shipping_cost}")
elif weight <= 5:
    shipping_cost = 100
    print(f"Shipping cost: ₹{shipping_cost}")
elif weight <= 10:
    shipping_cost = 200
    print(f"Shipping cost: ₹{shipping_cost}")
else:
    shipping_cost = 300
    print(f"Shipping cost: ₹{shipping_cost}")