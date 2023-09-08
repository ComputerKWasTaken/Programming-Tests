# Import the modules
import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Bouncy Balls")

# Define a class for the balls
class Ball:
    # Initialize the ball with its position, velocity, radius and color
    def __init__(self, x, y, vx, vy, r, c):
        self.x = x # x-coordinate of the center
        self.y = y # y-coordinate of the center
        self.vx = vx # x-component of the velocity
        self.vy = vy # y-component of the velocity
        self.r = r # radius of the ball
        self.c = c # color of the ball

    # Draw the ball on the screen
    def draw(self):
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r)

    # Update the position and velocity of the ball
    def update(self):
        # Move the ball according to its velocity
        self.x += self.vx
        self.y += self.vy

        # Apply gravity to the y-velocity of the ball
        gravity = 0.1 # increase this value to make the balls fall faster 
        self.vy += gravity

        # Bounce the ball off the edges of the screen with some damping factor
        damping = 0.9 # reduce this value to make the balls less bouncy
        if self.x - self.r < 0 or self.x + self.r > SCREEN_WIDTH:
            self.vx = -self.vx * damping
        if self.y - self.r < 0 or self.y + self.r > SCREEN_HEIGHT:
            self.vy = -self.vy * damping

# Create a list of balls with random attributes but fixed radius of 10 
balls = []
for i in range(50):
    x = random.randint(0, SCREEN_WIDTH) # random x-position
    y = random.randint(0, SCREEN_HEIGHT) # random y-position
    vx = random.randint(-5, 5) # random x-velocity
    vy = random.randint(-5, 5) # random y-velocity
    r = 10 # fixed radius 
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # random color
    balls.append(Ball(x, y, vx, vy, r, c))

# Define a variable to control the main loop
running = True

# Create a clock object to control the frame rate 
clock = pygame.time.Clock()

# Get the initial position of the window 
window_x, window_y = pygame.display.get_window_position()

# Main loop
while running:
    # Handle events by looping over the list of Event objects returned by pygame.event.get()
    for event in pygame.event.get():
        # If the user clicks on the close button, exit the loop and quit pygame 
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black color to erase previous drawings 
    screen.fill(BLACK)

    # Loop over each ball in the list and update its state and draw it on the screen 
    for ball in balls:
        ball.update()
        ball.draw()

    # Update the display with what has been drawn 
    pygame.display.flip()

    # Limit the frame rate to 60 FPS 
    clock.tick(120)

    # Get the current position of the window 
    new_window_x, new_window_y = pygame.display.get_window_position()

    # If the window has moved, adjust the positions of all balls accordingly 
    if new_window_x != window_x or new_window_y != window_y:
        for ball in balls:
            ball.x += new_window_x - window_x
            ball.y += new_window_y - window_y

        # Update the window position 
        window_x = new_window_x
        window_y = new_window_y

# Quit pygame 
pygame.quit()
