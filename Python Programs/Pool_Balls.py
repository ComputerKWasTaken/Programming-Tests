# Import modules
import math
import random
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
GRAVITY = 0.1

# Define a class for the balls
class Ball:
    # Initialize the ball with a position, a velocity and a color
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    # Draw the ball on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BALL_RADIUS)

    # Update the ball's position and velocity
    def update(self):
        # Apply gravity to the vertical velocity
        self.vy += GRAVITY

        # Update the position according to the velocity
        self.x += self.vx
        self.y += self.vy

        # Bounce off the edges of the screen
        if self.x < BALL_RADIUS or self.x > SCREEN_WIDTH - BALL_RADIUS:
            self.vx *= -1
        if self.y < BALL_RADIUS or self.y > SCREEN_HEIGHT - BALL_RADIUS:
            self.vy *= -1

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Create a list of balls with random positions, velocities and colors
balls = []
for i in range(10):
    x = random.randint(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
    y = random.randint(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    balls.append(Ball(x, y, vx, vy, color))

# Create a variable to store the selected ball (if any)
selected_ball = None

# Create a variable to store the mouse position
mouse_x = 0
mouse_y = 0

# Create a loop to run until the user quits
running = True
while running:
    # Makes speed normal
    clock = pygame.time.Clock()
    clock.tick(100)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a ball
            for ball in balls:
                dx = ball.x - event.pos[0]
                dy = ball.y - event.pos[1]
                if math.sqrt(dx * dx + dy * dy) < BALL_RADIUS:
                    # Select the ball
                    selected_ball = ball
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            # Deselect the ball
            selected_ball = None
        elif event.type == pygame.MOUSEMOTION:
            # Update the mouse position
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            # Move the selected ball with the arrow keys
            if selected_ball is not None:
                if event.key == pygame.K_LEFT:
                    selected_ball.vx -= 1
                elif event.key == pygame.K_RIGHT:
                    selected_ball.vx += 1
                elif event.key == pygame.K_UP:
                    selected_ball.vy -= 1
                elif event.key == pygame.K_DOWN:
                    selected_ball.vy += 1

    # Update the position of the selected ball according to the mouse position
    if selected_ball is not None:
        selected_ball.x = mouse_x
        selected_ball.y = mouse_y

    # Update and draw the balls
    screen.fill(BLACK)
    for ball in balls:
        ball.update()
        ball.draw(screen)
    pygame.display.flip()