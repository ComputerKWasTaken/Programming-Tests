# Define the player class
class Player:
    def __init__(self, shooting, passing, defending, goalkeeping, position):
        self.shooting = shooting
        self.passing = passing
        self.defending = defending
        self.goalkeeping = goalkeeping
        self.position = position

    def player_value(self):
        if self.position == 'ATT':
            value = self.shooting * 0.40 + self.passing * 0.30 + self.defending * 0.20 + self.goalkeeping * 0.10
        elif self.position == 'MID':
            value = self.shooting * 0.30 + self.passing * 0.40 + self.defending * 0.20 + self.goalkeeping * 0.10
        elif self.position == 'DEF':
            value = self.shooting * 0.10 + self.passing * 0.30 + self.defending * 0.40 + self.goalkeeping * 0.20
        elif self.position == 'GK':
            value = self.shooting * 0.05 + self.passing * 0.10 + self.defending * 0.15 + self.goalkeeping * 0.70
        return round(value*100000)

# Prompt the user for their position and stats
position = input('Enter your position (ATT, MID, DEF, GK): ').upper()
shooting = int(input('Enter your shooting stat: '))
passing = int(input('Enter your passing stat: '))
defending = int(input('Enter your defending stat: '))
goalkeeping = int(input('Enter your goalkeeping stat: '))

# Create a player object and calculate the player value
player1 = Player(shooting, passing, defending, goalkeeping, position)
value = player1.player_value()

# Format the result with commas and print it
formatted_value = f'{value:,}'
print(f'The player value is: ${formatted_value}')

# Prompt the user to decrease their player value by a certain percentage
decrease_percentage = float(input('Enter the percentage to decrease your total player value by (e.g., enter 80 for a decrease of 20%): '))
decreased_value = round(value * (decrease_percentage/100))

# Format the result with commas and print it
formatted_decreased_value = f'{decreased_value:,}'
print(f'Your decreased player value is: ${formatted_decreased_value}')

# Wait for the user to press Enter before closing
input('Press Enter to close')
