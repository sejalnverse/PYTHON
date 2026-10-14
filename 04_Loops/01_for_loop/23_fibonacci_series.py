terms = int(input("How many terms? "))

first = 0
second = 1

for i in range(terms):
    print(first, end=" ")

    next_number = first + second
    first = second
    second = next_number

print()