number = input("Enter a number: ")

reverse = ""

for digit in number:
    reverse = digit + reverse

print("Reversed number:", int(reverse))