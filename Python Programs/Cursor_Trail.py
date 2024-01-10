import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 5
FADEOUT_TIME = 1000  # in milliseconds
FALL_SPEED = 0.2  # pixels per millisecond

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# List to hold the circles
circles = []

# Easing function
def ease_out_expo(t):
    return (2 ** (10 * (t - 1)))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Add a new circle at the mouse position with random fall speed and fadeout time
    circles.append([list(mouse_pos), pygame.time.get_ticks(), random.uniform(0.1, 0.5), random.randint(500, 1500)])

    # Draw the background
    screen.fill(BACKGROUND_COLOR)

    # Draw all the circles
    for circle in circles:
        pos, spawn_time, fall_speed, fadeout_time = circle
        time_alive = pygame.time.get_ticks() - spawn_time

        if time_alive > fadeout_time:
            # If the circle has been alive longer than the fadeout time, remove it
            circles.remove(circle)
        else:
            # Otherwise, draw the circle with an alpha value based on its age
            alpha = int(255 - (255 * time_alive / fadeout_time))
            faded_color = CIRCLE_COLOR + (alpha,)

            # Apply the easing function to the y position
            pos[1] += fall_speed * time_alive * ease_out_expo(time_alive / fadeout_time)

            # Create a temporary surface, draw the circle on it, and then blit it onto the main screen with the alpha value
            temp_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(temp_surface, faded_color, [int(x) for x in pos], CIRCLE_RADIUS)
            screen.blit(temp_surface, (0, 0))

    # Update the display
    pygame.display.flip()