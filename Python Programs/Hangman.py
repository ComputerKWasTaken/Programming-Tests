# A simple Python program for a Hangman game
# The chosen word that needs to be guessed is chosen from a list that I'll add words to later

import random

# A list of words to choose from
words = ["apple", "banana", "cat", "dog", "elephant", "fish", "giraffe", "hat", "ice", "joke", "kite", "lion", "mouse", "nest", "orange", "pear", "queen", "rainbow", "star", "tree", "umbrella", "vase", "water", "x-ray", "yarn", "zebra"]

# Pick a random word from the list
word = random.choice(words)

# The number of guesses allowed
guesses = 10

# The letters that have been guessed
guessed = []

# The word as a list of underscores
hidden = ["_"] * len(word)

# A function to update the hidden word based on the guessed letters
def update_hidden():
  global hidden
  for i in range(len(word)):
    if word[i] in guessed:
      hidden[i] = word[i]

# A function to check if the game is over
def is_over():
  global guesses
  global hidden
  if guesses == 0:
    print("You lose! The word was", word)
    return True
  elif "_" not in hidden:
    print("You win! The word was", word)
    return True
  else:
    return False

# The main loop of the game
while not is_over():
  # Print the hidden word and the number of guesses left
  print(" ".join(hidden))
  print("You have", guesses, "guesses left")

  # Ask the user to guess a letter
  letter = input("Guess a letter: ").lower()

  # Check if the letter is valid and has not been guessed before
  if len(letter) != 1 or not letter.isalpha():
    print("Invalid input")
  elif letter in guessed:
    print("You already guessed that letter")
  else:
    # Add the letter to the guessed letters
    guessed.append(letter)

    # Check if the letter is in the word
    if letter in word:
      print("Correct!")
      # Update the hidden word
      update_hidden()
    else:
      print("Wrong!")
      # Reduce the number of guesses by one
      guesses -= 1