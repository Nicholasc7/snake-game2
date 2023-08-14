import pygame
import random
from board import Grid
from apple import Apple
from snake import Snake


#----------GLOBAL----------#
pygame.init()
screen = pygame.display.set_mode((900, 900))
clock = pygame.time.Clock()
running = True
dt = 0
cycle = 0
# Apple initilize
a1 = Apple(screen)
APPLE_CENTER = a1.findCenter()
# Snake initialize
s1 = Snake(screen)
SNAKE_SPAWN_COR = s1.spawnCor()
#----------GLOBAL----------#


#----------GAME LOOP----------#
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Board Setup
    screen.fill("purple")
    grid = Grid(screen, "lightgrey")
    grid.drawGrid()

    # Food Setup
    apple = Apple(screen)
    apple.spawnApple(APPLE_CENTER)

    # Snake Setup
    snake = Snake(screen)
    snake.spawnHead(SNAKE_SPAWN_COR)

    # Snake Controls
    snake.move(keys)


    pygame.display.flip()
pygame.quit()