import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 500
BACKGROUND_COLOR = pygame.Color('black')
CIRCLE_COLOR = pygame.Color('white')
MAX_DISTANCE = math.sqrt(WIDTH**2 + HEIGHT**2)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Make the window resizable

# Set the number of circles
num_circles = 10  # Change this value for testing

# Create a list of circles
circles = [(i * WIDTH // (num_circles-1), j * HEIGHT // (num_circles-1)) for i in range(num_circles) for j in range(num_circles)]

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:  # The window has been resized
            WIDTH, HEIGHT = event.w, event.h
            MAX_DISTANCE = math.sqrt(WIDTH**2 + HEIGHT**2)
            circles = [(i * WIDTH // (num_circles-1), j * HEIGHT // (num_circles-1)) for i in range(num_circles) for j in range(num_circles)]

    # Fill the background
    window.fill(BACKGROUND_COLOR)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw each circle
    for x, y in circles:
        # Calculate the distance to the mouse
        distance = math.sqrt((x - mouse_pos[0])**2 + (y - mouse_pos[1])**2)

        # Calculate the color based on the distance
        color = int(255 * (1 - (distance / MAX_DISTANCE)**2))  # Increase the magnitude of the inverse square law

        # Draw the circle
        pygame.draw.circle(window, (color, color, color), (x, y), 20)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
