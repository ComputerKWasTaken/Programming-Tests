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
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a font object
font = pygame.font.Font(None, 32)

# Create a text input box
input_box = pygame.Rect(WIDTH // 2, HEIGHT // 2, 140, 32)
text = ''
active = False
num_circles = 10  # Initialize num_circles with a default value

# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    num_circles = int(text)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Fill the background
    window.fill(BACKGROUND_COLOR)

    # Draw the input box
    pygame.draw.rect(window, CIRCLE_COLOR, input_box, 2)
    txt_surface = font.render(text, True, CIRCLE_COLOR)
    window.blit(txt_surface, (input_box.x+5, input_box.y+5))

    # Update the display
    pygame.display.flip()

# Create a list of circles
circles = [(i * WIDTH // num_circles, j * HEIGHT // num_circles) for i in range(num_circles) for j in range(num_circles)]

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