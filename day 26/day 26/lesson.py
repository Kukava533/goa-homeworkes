from random import randint

def guess_game(max_guesses_allowed, diff):
    if diff == "H":
        secret_number = randint(1, 100)
    else:
        secret_number = randint(1, 5)

    guess_count = 0
    user_guess = 0
    guess_list = []  # Initialize an empty list to store previous guesses

    while guess_count < max_guesses_allowed:
        user_guess = int(input("Enter your guess: "))

        if user_guess in guess_list:
            print("You already guessed this number.")
        else:
            guess_list.append(user_guess)  # Add the new guess to the list
            print(guess_list)

            guess_count += 1  # Increase guess_count by 1

            if user_guess == secret_number:
                print("Congratulations! You win!")
                print("You took", guess_count, "guesses!")
                return
            elif user_guess > secret_number:
                print("Sorry, your guess was too high")
            elif user_guess < secret_number:
                print("Sorry, your guess was too low")

print("Welcome to the guessing game!")
max_guess = int(input("Enter the maximum number of guesses allowed:"))
slct_diff = str(input("Enter difficulty E(asy) or H(ard): "))
guess_game(max_guess, slct_diff)