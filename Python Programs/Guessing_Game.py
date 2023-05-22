import random
import time

def get_guess(player):
    if player == "bot":
        return random.randint(min_guess, max_guess)
    else:
        return int(input("Enter your guess: "))

# The number to guess
number = random.randint(1, 100)

# The number of chances left
chances = 10

# The minimum possible guess
min_guess = 1

# The maximum possible guess
max_guess = 100

# The flag to indicate if the game is over
game_over = False

player = input("Do you want to play or let the bot play? (Enter 'me' or 'bot'): ")

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

    time.sleep(1.5)