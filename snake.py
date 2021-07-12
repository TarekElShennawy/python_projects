import pygame
import time
import random

pygame.init()

#Setting up game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))

pygame.display.update()
pygame.display.set_caption("Snake")

#Defining color
green=(0,255,0)
red=(255,0,0)
white=(255, 255, 255)
black=(0,0,0)
snake_size = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)

#Define snake size
def snake_properties(snake_size, snake_list_length):
    for x in snake_list_length:
        pygame.draw.rect(window, green, [x[0], x[1], snake_size, snake_size])

#Score calculate
def the_score(score):
    score_value = score_font.render("Score: " + str(score), True, green)
    window.blit(score_value, [0, 0])

#Game Over message 
def message(m, color):
    msg = font_style.render(m, True, color)
    window.blit(msg, [window_width/3, window_height/3])
    
    # Main loop function
def mainLoop():
    x1 = window_width/2
    y1 = window_height/2
    x1_change = 0
    y1_change = 0

    snake_list_length = []
    snake_length = 1

    snackx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    snacky = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
    
    game_over = False
    game_close = False
    
    while not game_over:
        
        while game_close == True:
            window.fill(black)
            message("Game over! Press A to try again or Q to quit!", red)
            the_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        mainLoop()
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        # If statement to ensure snake died if it hits the border
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red,[snackx, snacky, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list_length.append(snake_head)
        
        if len( snake_list_length ) > snake_length:
            del snake_list_length[0]

        for x in snake_list_length[:-1]:
            if x == snake_head:
                game_close = True
    
        snake_properties(snake_size, snake_list_length)
        
        pygame.draw.rect(window,green,[x1,y1,snake_size,snake_size])
        the_score(snake_length - 1)
        pygame.display.update()

        if x1 == snackx and y1 == snacky:
            print("Yum!")
            snackx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            snacky = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            snake_length += 1
            
        clock.tick(snake_speed)


    time.sleep(2)
        
    #End Loop
    pygame.quit()
    quit()

mainLoop()
