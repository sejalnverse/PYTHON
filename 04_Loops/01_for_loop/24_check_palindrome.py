text = input("Enter a word: ")

reverse = ""

for letter in text:
    reverse = letter + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")