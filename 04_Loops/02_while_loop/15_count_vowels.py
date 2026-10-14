text = input("Enter a string: ")

i = 0
count = 0

while i < len(text):
    if text[i].lower() in "aeiou":
        count = count + 1

    i = i + 1

print("Total vowels:", count)