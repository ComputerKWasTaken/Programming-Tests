# Import pygame module
import pygame

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create a window with size 800x600
window = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption("Bouncing Ball")

# Create a ball object with radius 20 and color red
ball = pygame.draw.circle(window, (255, 0, 0), (400, 300), 20)

# Define the initial velocity and acceleration of the ball
vx = 0 # Horizontal velocity
vy = 5 # Vertical velocity
ax = 0 # Horizontal acceleration
ay = 0.2 # Vertical acceleration (gravity)

# Define the coefficient of restitution (bounce factor)
e = 0.8

# Define a boolean variable to indicate if the game is running
running = True

# Main game loop
while running:
    # Fill the window with black color
    window.fill((0, 0, 0))

    # Slow the game down a little bit
    clock.tick(100)

    # Draw the ball on the window
    pygame.draw.circle(window, (255, 0, 0), ball.center, ball.width // 2)

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game loop
        if event.type == pygame.QUIT:
            running = False

        # If an arrow key is pressed, update the velocity of the ball accordingly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vx -= 1
            elif event.key == pygame.K_RIGHT:
                vx += 1
            elif event.key == pygame.K_UP:
                vy -= 5

    # Update the position of the ball using kinematics equations
    ball.x += vx # x = x + vx * dt (dt = 1)
    ball.y += vy # y = y + vy * dt (dt = 1)
    vx += ax # vx = vx + ax * dt (dt = 1)
    vy += ay # vy = vy + ay * dt (dt = 1)

    # Check if the ball hits the boundaries of the window and bounce it back
    if ball.left < 0 or ball.right > window.get_width():
        vx = -vx * e # Reverse and reduce the horizontal velocity
        ball.x = max(0, min(ball.x, window.get_width() - ball.width)) # Keep the ball inside the window

    if ball.top < 0 or ball.bottom > window.get_height():
        vy = -vy * e # Reverse and reduce the vertical velocity
        ball.y = max(0, min(ball.y, window.get_height() - ball.height)) # Keep the ball inside the window

# Quit pygame
pygame.quit()