num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
num3 = int(input("enter third number : "))
if num1 > num2 and num1 > num3:
    print("first number is largest")
elif num2 > num1 and num2 > num3:
    print("second number is largest")
else:
    print("third number is largest")