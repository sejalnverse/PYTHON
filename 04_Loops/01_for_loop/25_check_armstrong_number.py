number = input("Enter a number: ")

power = len(number)
total = 0

for digit in number:
    total = total + int(digit) ** power

if total == int(number):
    print("Armstrong number")
else:
    print("Not an Armstrong number")