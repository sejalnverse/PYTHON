a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilateral triangle")
        else:
            if a == b or b == c or a == c:
                print("Isosceles triangle")
            else:
                print("Scalene triangle")
    else:
        print("Invalid triangle")
else:
    print("All sides must be positive")