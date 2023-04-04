# Import pygame and random modules
import pygame
import random

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BALL_NUMBER = 10

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Create a list of balls with random attributes
balls = []
for i in range(BALL_NUMBER):
    # Choose a random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Choose a random position within the bounds of the window
    x = random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
    y = random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)
    # Choose a random velocity
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    # Create a ball object and append it to the list
    ball = pygame.draw.circle(screen, color, (x, y), BALL_RADIUS)
    ball.vx = vx
    ball.vy = vy
    balls.append(ball)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit if the user closes the window or presses ESC
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Update the screen
    screen.fill((0, 0, 0)) # Fill the screen with black
    for ball in balls:
        # Move the ball according to its velocity
        ball.x += ball.vx
        ball.y += ball.vy
        # Bounce the ball off the edges of the window
        if ball.x < BALL_RADIUS or ball.x > SCREEN_WIDTH - BALL_RADIUS:
            ball.vx = -ball.vx
        if ball.y < BALL_RADIUS or ball.y > SCREEN_HEIGHT - BALL_RADIUS:
            ball.vy = -ball.vy
        # Check for collisions with other balls
        for other in balls:
            if other != ball and pygame.sprite.collide_circle(ball, other):
                # Swap the velocities of the colliding balls
                ball.vx, other.vx = other.vx, ball.vx
                ball.vy, other.vy = other.vy, ball.vy
        # Draw the ball on the screen
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()