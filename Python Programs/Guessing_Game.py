import random
import time

def get_guess(player):
    if player == "bot":
        return random.randint(min_guess, max_guess)
    else:
        return int(input("Enter your guess: "))

# The number to guess
number = random.randint(1, 100)

# The flag to indicate if the game is over
game_over = False

player = input("Do you want to play or let the bot play? (Enter 'me' or 'bot'): ")

# The number of chances left
if player == "bot":
    chances = 8
else:
    chances = 10

# The minimum possible guess
min_guess = 1

# The maximum possible guess
max_guess = 100

# The list of previous guesses
previous_guesses = []

while not game_over:
    # The player's guess
    guess = get_guess(player)

    # Print the guess
    print(f"The guess is {guess}.")

    # Check if the guess is correct
    if guess == number:
        # The player wins
        print("You got it!")
        game_over = True
    else:
        # Check if the guess is valid
        if guess in previous_guesses:
            print(f"You already guessed {guess}. Try again.")
        elif guess < min_guess:
            print(f"Your guess is below the minimum possible guess of {min_guess}. Try again.")
        elif guess > max_guess:
            print(f"Your guess is above the maximum possible guess of {max_guess}. Try again.")
        else:
            # The player loses a chance
            chances -= 1

            # Check if the player has no more chances
            if chances == 0:
                # The player loses
                print(f"Sorry, the number was {number}.")
                game_over = True
            else:
                # The player can try again
                if guess < number:
                    print(f"Wrong. Your guess is too low. You have {chances} chances left.")
                    min_guess = guess + 1
                else:
                    print(f"Wrong. Your guess is too high. You have {chances} chances left.")
                    max_guess = guess - 1

            # Add the valid guess to the list of previous guesses
            previous_guesses.append(guess)

    time.sleep(1.5)
