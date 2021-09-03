# create the classical snake game
# using pygame library

import pygame
import random
import time

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

# snake
snake_img = pygame.image.load('snake.png')
snake_x = 370
snake_y = 480
snake_x_change = 0
snake_y_change = 0

# food
food_img = pygame.image.load('food.png')
food_x = random.randint(0, 735)
food_y = random.randint(0, 535)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def snake(x, y):
    screen.blit(snake_img, (x, y))


def food(x, y):
    screen.blit(food_img, (x, y))


# game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -1
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                snake_x_change = 1
                snake_y_change = 0
            if event.key == pygame.K_UP:
                snake_y_change = -1
                snake_x_change = 0
            if event.key == pygame.K_DOWN:
                snake_y_change = 1
                snake_x_change = 0

    # snake movement
    snake_x += snake_x_change
    snake_y += snake_y_change

    # snake boundaries
    if snake_x <= 0:
        snake_x = 800
    elif snake_x >= 800:
        snake_x = 0
    elif snake_y <= 0:
        snake_y = 600
    elif snake_y >= 600:
        snake_y = 0

    # food
    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score_value += 1
        food_x = random.randint(0, 735)
        food_y = random.randint(0, 535)

    snake(snake_x, snake_y)
    food(food_x, food_y)
    show_score(text_x, text_y)
    pygame.display.update()