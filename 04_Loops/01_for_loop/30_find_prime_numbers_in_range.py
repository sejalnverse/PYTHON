start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")

for number in range(max(2, start), end + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number)