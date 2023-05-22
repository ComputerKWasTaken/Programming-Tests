# Define the weights for each stat based on the position
weights = {
    "ATT": {"shooting": 0.5, "passing": 0.3, "defending": 0.1, "goalkeeping": 0.1},
    "MID": {"shooting": 0.2, "passing": 0.4, "defending": 0.3, "goalkeeping": 0.1},
    "DEF": {"shooting": 0.1, "passing": 0.3, "defending": 0.6, "goalkeeping": 0.1},
    "GK": {"shooting": 0.1, "passing": 0.1, "defending": 0.1, "goalkeeping": 0.7},
}

# Define the scale or formula to convert the rating into a value
def value(rating):
    # Use a linear scale where each point of rating is worth $1000
    return rating * 100000
    # Or use an exponential scale where each point of rating is worth $1000 times the rating itself
    # return rating * 100000 * rating
    # Or use any other function that suits your needs

# Define a function to calculate the value of a player based on their position and stats
def calculate_value(position, shooting, passing, defending, goalkeeping):
    # Get the weights for the position
    w = weights[position]
    # Calculate the overall rating by multiplying each stat by its weight and adding them up
    rating = (shooting * w["shooting"]) + (passing * w["passing"]) + (defending * w["defending"]) + (goalkeeping * w["goalkeeping"])
    # Convert the rating into a value using the scale or formula
    return value(rating)

# Ask the user to input their position and stats
position = input("Enter your position (ATT/MID/DEF/GK): ").upper()
shooting = int(input("Enter your shooting: "))
passing = int(input("Enter your passing: "))
defending = int(input("Enter your defending: "))
goalkeeping = int(input("Enter your goalkeeping: "))

# Print the value of the player based on their input
print(f"The value of a {position} with {shooting} shooting, {passing} passing, {defending} defending and {goalkeeping} goalkeeping is ${calculate_value(position, shooting, passing, defending, goalkeeping):,.2f}")