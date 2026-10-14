secret_number = 7

while True:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")