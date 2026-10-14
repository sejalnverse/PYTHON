text = input("Enter a string: ")

count = 0

for letter in text:
    if letter.lower() in "aeiou":
        count = count + 1

print("Total vowels:", count)