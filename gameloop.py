import pygame
import random
from board import Grid
from bomb import Bomb
from snake import Snake
from collision import Collide


#----------GLOBAL----------#
pygame.init()
screen = pygame.display.set_mode((960, 960))
clock = pygame.time.Clock()
running = True
dt = 0
cycle = 0
grid = Grid(screen, "black")
padding = grid.padding
collision = 0

# Bomb initilize
b1 = Bomb(screen)
BOMB_CENTER = b1.findCenter()
ARROW_DIR = b1.spawnDir(screen, BOMB_CENTER)



# Snake initialize
s1 = Snake(screen, BOMB_CENTER)
SNAKE_COR = s1.spawnCor()
keyLog = {"w":0, "d":0, "s":0, "a":0}
        
#----------GLOBAL----------#


# TODO: Fix bomb line so it moves with the circle on collision, line isn't spawning at updated bombCenter or the bombCenter isn't updating


#----------GAME LOOP----------#
def gameLoop(keyLog):
    updatedArrows = b1.returnArrowCombObjects(screen, BOMB_CENTER, ARROW_DIR)
    # Board Setup
    screen.fill("white")
    grid = Grid(screen, "darkgrey")
    grid.drawGrid()

    # Bomb Setup
    bomb = Bomb(screen)
    bomb.spawnCircle(BOMB_CENTER)

    # Snake Setup & Movement
    snake = Snake(screen, BOMB_CENTER)
    snake.handleKeyLog(keys, keyLog)
    snake.head(keyLog, SNAKE_COR)

    # Handle Collision
    col = Collide(screen, keyLog, ARROW_DIR, BOMB_CENTER, SNAKE_COR)
    if col.collide:
        updatedArrows = b1.returnArrowCombObjects
    bomb.drawUpdatedArrows(screen, updatedArrows, ARROW_DIR)

    pygame.display.flip()
#----------GAME LOOP----------#

#TODO: update the global variable prevArrows by changing its value through arithmetic. Find the difference, etc 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    gameLoop(keyLog)

    dt = clock.tick(11) / 1000

pygame.quit()