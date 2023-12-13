import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 500
BACKGROUND_COLOR = pygame.Color('black')
CIRCLE_COLOR = pygame.Color('white')
NUM_CIRCLES = 10
MAX_DISTANCE = math.sqrt(WIDTH**2 + HEIGHT**2)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a list of circles
circles = [(i * WIDTH // NUM_CIRCLES, j * HEIGHT // NUM_CIRCLES) for i in range(NUM_CIRCLES) for j in range(NUM_CIRCLES)]

# Game loop
running = True
while running:
    # Fill the background
    window.fill(BACKGROUND_COLOR)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw each circle
    for x, y in circles:
        # Calculate the distance to the mouse
        distance = math.sqrt((x - mouse_pos[0])**2 + (y - mouse_pos[1])**2)

        # Calculate the color based on the distance
        color = 255 - int(255 * distance / MAX_DISTANCE)

        # Draw the circle
        pygame.draw.circle(window, (color, color, color), (x, y), 20)

    # Update the display
    pygame.display.flip()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
