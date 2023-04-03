// Typescript code for generating a random 4-digit pin that the player has to guess
let pin = Math.floor(Math.random() * 10000).toString().padStart(4, "0");
let guesses = 10;

// A function to check the player's guess and return an array of colors
function checkGuess(guess: string): string[] {
  let colors: string[] = [];
  for (let i = 0; i < 4; i++) {
    if (guess[i] === pin[i]) {
      // The correct number is in the right spot, it'll be green
      colors.push("green");
    } else if (pin.includes(guess[i])) {
      // The number guessed is there but not in the right spot, it'll be yellow
      colors.push("yellow");
    } else {
      // The number isn't in the pin, it'll be gray
      colors.push("gray");
    }
  }
  return colors;
}

// A loop to get the player's input and display the result
while (guesses > 0) {
    let guess = prompt("Enter a 4-digit number");
    if (guess === null) {
      // Handle the case where the user cancels the prompt
      break;
    }
    if (guess === pin) {
      alert("You win!");
      break;
    } else {
      let colors = checkGuess(guess);
      alert(`Your guess: ${guess}\nColors: ${colors.join(", ")}`);
      guesses--;
    }
  }
  
  if (guesses === 0) {
    alert(`You lose! The pin was ${pin}`);
  }