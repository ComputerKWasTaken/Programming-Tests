import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set gravity, number of balls, min and max ball size, and coefficient of restitution
gravity = 0.1
num_balls = 25
min_ball_size = 15
max_ball_size = 25
restitution = 0.95

# Ball class
class Ball:
    def __init__(self):
        self.size = random.randint(min_ball_size, max_ball_size)
        self.x = random.randint(self.size, size[0] - self.size)
        self.y = random.randint(self.size, size[1] - self.size)
        self.change_x = random.uniform(-3, 3)
        self.change_y = random.uniform(-3, 3)
        # Having the minimum random number color be 25 prevents balls that are too difficult to see (too dark)
        self.color = (random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

        # Add gravity
        self.change_y += gravity

        if self.x > size[0] - self.size or self.x < self.size:
            self.change_x *= -1

        if self.y > size[1] - self.size:
            self.y = size[1] - self.size
            self.change_y *= -restitution

balls = []
for i in range(num_balls):
    while True:
        new_ball = Ball()
        if not any(math.hypot(ball.x - new_ball.x, ball.y - new_ball.y) < ball.size + new_ball.size for ball in balls):
            balls.append(new_ball)
            break

# -------- Main Program Loop -----------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # --- Game logic should go here

    # --- Drawing code should go here
    screen.fill(BLACK)

    for ball in balls:
        ball.draw()
        ball.move()

    # Check for collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[i].x - balls[j].x
            dy = balls[i].y - balls[j].y
            distance = math.hypot(dx, dy)

            if distance < balls[i].size + balls[j].size:
                angle = math.atan2(dy, dx)
                speed_i = math.hypot(balls[i].change_x, balls[i].change_y)
                speed_j = math.hypot(balls[j].change_x, balls[j].change_y)
                direction_i = math.atan2(balls[i].change_y, balls[i].change_x)
                direction_j = math.atan2(balls[j].change_y, balls[j].change_x)
                new_speed_i_x = speed_i * math.cos(direction_i - angle) * (balls[i].size - balls[j].size) / (balls[i].size + balls[j].size) + speed_j * math.cos(direction_j - angle) * (2 * balls[j].size) / (balls[i].size + balls[j].size)
                new_speed_i_y = speed_i * math.sin(direction_i - angle) * (balls[i].size - balls[j].size) / (balls[i].size + balls[j].size) + speed_j * math.sin(direction_j - angle) * (2 * balls[j].size) / (balls[i].size + balls[j].size)
                new_speed_j_x = speed_i * math.cos(direction_i - angle) * (2 * balls[i].size) / (balls[i].size + balls[j].size) + speed_j * math.cos(direction_j - angle) * (balls[j].size - balls[i].size) / (balls[i].size + balls[j].size)
                new_speed_j_y = speed_i * math.sin(direction_i - angle) * (2 * balls[i].size) / (balls[i].size + balls[j].size) + speed_j * math.sin(direction_j - angle) * (balls[j].size - balls[i].size) / (balls[i].size + balls[j].size)
                balls[i].change_x = new_speed_i_x * math.cos(angle) - new_speed_i_y * math.sin(angle)
                balls[i].change_y = new_speed_i_y * math.cos(angle) + new_speed_i_x * math.sin(angle)
                balls[j].change_x = new_speed_j_x * math.cos(angle) - new_speed_j_y * math.sin(angle)
                balls[j].change_y = new_speed_j_y * math.cos(angle) + new_speed_j_x * math.sin(angle)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
