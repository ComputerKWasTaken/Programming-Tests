import random

# Python code for generating a random 4-digit pin that the player has to guess
pin = str(random.randint(0, 9999)).zfill(4)
guesses = 10

# A function to check the player's guess and return an array of colors
def check_guess(guess):
    colors = []
    for i in range(4):
        if guess[i] == pin[i]:
            # The correct number is in the right spot, it'll be green
            colors.append("green")
        elif guess[i] in pin:
            # The number guessed is there but not in the right spot, it'll be yellow
            colors.append("yellow")
        else:
            # The number isn't in the pin, it'll be gray
            colors.append("gray")
    return colors

# A loop to get the player's input and display the result
while guesses > 0:
    guess = input("Enter a 4-digit number: ")
    if guess == pin:
        print("You win!")
        break
    else:
        colors = check_guess(guess)
        print(f"Your guess: {guess}\nColors: {', '.join(colors)}")
        guesses -= 1

if guesses == 0:
    print(f"You lose! The correct pin was {pin}")