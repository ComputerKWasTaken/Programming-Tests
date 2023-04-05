import pygame 
import random 
import math 
 # Define some colors and constants 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 600 
BALL_RADIUS = 10 
BALL_SPEED = 5 
GRAVITY = 0.5 
 # Initialize pygame and create a window 
pygame.init() 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Bouncing Balls") 
clock = pygame.time.Clock() 
 # Create a list of balls 
balls = [] 
for i in range(20): 
    # Randomize the position, direction and color of each ball 
    x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS) 
    y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS) 
     # Check if the ball collides with another ball 
    while any(math.hypot(x - ball["x"], y - ball["y"]) < 2 * BALL_RADIUS for ball in balls): 
        x = random.randint(BALL_RADIUS, WINDOW_WIDTH - BALL_RADIUS) 
        y = random.randint(BALL_RADIUS, WINDOW_HEIGHT - BALL_RADIUS) 
    dx = random.choice([-1, 1]) * BALL_SPEED 
    dy = random.choice([-1, 1]) * BALL_SPEED 
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
     # Create a dictionary to store the ball's attributes 
    ball = { 
        "x": x, 
        "y": y, 
        "dx": dx, 
        "dy": dy, 
        "color": color, 
        "dragged": False 
    } 
     # Add the ball to the list 
    balls.append(ball) 
def normalize_vector(vx, vy): 
    magnitude = math.hypot(vx, vy) 
    return vx/magnitude, vy/magnitude 
 # Main loop 
running = True 
while running: 
    # Handle events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            # Quit the program 
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            # Check if any ball is clicked 
            for ball in balls: 
                # Get the distance between the mouse position and the ball's center 
                mouse_x, mouse_y = pygame.mouse.get_pos() 
                dist = math.hypot(mouse_x - ball["x"], mouse_y - ball["y"]) 
                # If the distance is less than the ball's radius, set the ball as dragged 
                if dist < BALL_RADIUS: 
                    ball["dragged"] = True 
                    break 
        elif event.type == pygame.MOUSEBUTTONUP: 
            # Release any dragged ball 
            for ball in balls: 
                if ball["dragged"]: 
                    ball["dragged"] = False 
     # Update the state of each ball 
    for i in range(len(balls)): 
        # Get the current ball 
        ball1 = balls[i] 
        # If the ball is dragged, set its position to the mouse position 
        if ball1["dragged"]: 
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            ball1["x"] = mouse_x 
            ball1["y"] = mouse_y 
        else: 
            # Move the ball according to its direction and add gravity 
            ball1["x"] += ball1["dx"] 
            ball1["y"] += ball1["dy"] 
            ball1["dy"] += GRAVITY 
            # Bounce the ball off the edges of the window with a coefficient of restitution of 1 
            if ball1["x"] < BALL_RADIUS or ball1["x"] > WINDOW_WIDTH - BALL_RADIUS: 
                ball1["dx"] *= -1 
            if ball1["y"] < BALL_RADIUS or ball1["y"] > WINDOW_HEIGHT - BALL_RADIUS: 
                ball1["dy"] *= -1 
         # Check for collisions with other balls 
        for j in range(i + 1, len(balls)): 
            # Get another ball 
            ball2 = balls[j] 
            # Get the distance between the two balls' centers 
            dist = math.hypot(ball1["x"] - ball2["x"], ball1["y"] - ball2["y"]) 
            # If the distance is less than twice the radius, bounce them off each other 
            if dist < 2 * BALL_RADIUS: 
                # Get the collision vector 
                collision_vx, collision_vy = ball2["x"] - ball1["x"], ball2["y"] - ball1["y"] 
                collision_vx, collision_vy = normalize_vector(collision_vx, collision_vy) 
                # Compute the new velocities after collision 
                old_v1 = (ball1["dx"] * collision_vx) + (ball1["dy"] * collision_vy) 
                old_v2 = (ball2["dx"] * collision_vx) + (ball2["dy"] * collision_vy) 
                ball1["dx"] += (old_v2 - old_v1) * collision_vx 
                ball1["dy"] += (old_v2 - old_v1) * collision_vy 
                ball2["dx"] += (old_v1 - old_v2) * collision_vx 
                ball2["dy"] += (old_v1 - old_v2) * collision_vy 
     # Clear the screen and draw each ball 
    screen.fill(BLACK) 
    for ball in balls: 
        pygame.draw.circle(screen, ball["color"], (int(ball["x"]), int(ball["y"])), BALL_RADIUS) 
     # Update the display and limit the frame rate 
    pygame.display.flip() 
    clock.tick(60) 
 # Close the window and quit the program 
pygame.quit()
