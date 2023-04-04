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

# Define a function to check for collisions between two balls
def collide(ball1, ball2):
    # Calculate the distance between the centers of the balls
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y
    distance = (dx**2 + dy**2)**0.5
    # Return True if the distance is less than or equal to the sum of the radii
    return distance <= (BALL_RADIUS + BALL_RADIUS)

# Define a function to handle collisions between two balls
def bounce(ball1, ball2):
    # Swap the velocities of the balls along the collision axis
    nx = ball1.x - ball2.x
    ny = ball1.y - ball2.y
    n_length = (nx**2 + ny**2)**0.5
    nx /= n_length
    ny /= n_length
    v1n = ball1.vx * nx + ball1.vy * ny
    v2n = ball2.vx * nx + ball2.vy * ny
    v1t = -ball1.vx * ny + ball1.vy * nx
    v2t = -ball2.vx * ny + ball2.vy * nx
    ball1.vx = v2n * nx - v1t * ny
    ball1.vy = v2n * ny + v1t * nx
    ball2.vx = v1n * nx - v2t * ny
    ball2.vy = v1n * ny + v2t * nx

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        # Quit if the user closes the window or presses ESC
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # Update the positions and velocities of the balls
    for ball in balls:
        # Move the ball according to its velocity
        ball.x += ball.vx
        ball.y += ball.vy

        # Bounce the ball off the edges of the window if it goes out of bounds
        if ball.x < BALL_RADIUS or ball.x > SCREEN_WIDTH - BALL_RADIUS:
            ball.vx *= -1

        if ball.y < BALL_RADIUS or ball.y > SCREEN_HEIGHT - BALL_RADIUS:
            ball.vy *= -1

        # Check for collisions with other balls and handle them accordingly
        for other_ball in balls:
            if other_ball != ball and collide(ball, other_ball):
                bounce(ball, other_ball)

        # Redraw the ball on the screen with its new position and color
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), BALL_RADIUS)

    # Update the display and wait for some time to control the frame rate
    pygame.display.flip()
    pygame.time.wait(10)

# Quit pygame and exit the program
pygame.quit()