# This is a python PyGame code for a game in which to have to reach a certain number through 200-300 by rolling dice within one minute
# Pressing O rolls positively, pressing P rolls negatively. The game ends when you hit the target number.

import time
import pygame
import random

pygame.init()
window = pygame.display.set_mode((500, 500)) # create a window of size 500x500
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 32) # create a font object for displaying text

target = random.randint(200, 300) # choose a random target number between 200 and 300
score = 0 # initialize the score to zero
time_left = 45 # initialize the time left to 45 seconds
game_over = False # initialize the game over flag to False

while not game_over: # main game loop
    clock.tick(60) # limit the frame rate to 60 FPS
    current_time = pygame.time.get_ticks() # get the current time in milliseconds
    time_left = 45 - (current_time // 1000) # calculate the time left in seconds

    for event in pygame.event.get(): # handle events
        if event.type == pygame.QUIT: # if the user clicks the close button
            game_over = True # end the game loop
        if event.type == pygame.KEYDOWN: # if the user presses a key
            if event.key == pygame.K_o: # if the user presses O
                score += random.randint(1, 6) # roll a positive dice and add it to the score
            if event.key == pygame.K_p: # if the user presses P
                score -= random.randint(1, 6) # roll a negative dice and subtract it from the score

    window.fill((255, 255, 255)) # fill the window with white color

    target_text = font.render(f"Target: {target}", True, (0, 0, 0)) # create a text object for the target number
    score_text = font.render(f"Score: {score}", True, (0, 0, 0)) # create a text object for the score
    time_text = font.render(f"Time: {time_left}", True, (0, 0, 0)) # create a text object for the time left

    window.blit(target_text, (50, 50)) # draw the target text on the window
    window.blit(score_text, (50, 100)) # draw the score text on the window
    window.blit(time_text, (50, 150)) # draw the time text on the window

    if score == target: # if the score matches the target number
        result_text = font.render("You win!", True, (0, 255, 0)) # create a text object for winning message
        window.blit(result_text, (200, 250)) # draw the winning message on the window
        time.sleep(5) # wait for 5 seconds
        game_over = True # end the game loop

    if time_left <= 0: # if the time runs out
        result_text = font.render("You lose!", True, (255, 0, 0)) # create a text object for losing message
        window.blit(result_text, (200, 250)) # draw the losing message on the window
        time.sleep(5) # wait for 5 seconds
        game_over = True # end the game loop

    pygame.display.flip() # update the display

pygame.quit() # quit pygame