num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = abs(num1)
b = abs(num2)

gcd = 0

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD:", gcd)