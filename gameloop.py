import pygame
import random
from board import Grid
from bomb import Bomb
from snake import Snake
from collision import Hitbox


#----------GLOBAL----------#
pygame.init()
screen = pygame.display.set_mode((960, 960))
clock = pygame.time.Clock()
running = True
dt = 0
cycle = 0
grid = Grid(screen, "black")
padding = grid.padding

# Bomb initilize
b1 = Bomb(screen)
BOMB_CENTER = b1.findCenter()
ARROW_DIR = b1.spawnDir(screen, BOMB_CENTER)
ARROW_COMB_OBJECTS = b1.returnArrowCombObjects(screen, BOMB_CENTER,ARROW_DIR)

# Snake initialize
s1 = Snake(screen)
SNAKE_COR = s1.spawnCor()
keyLog = {"w":0, "a":0, "s":0, "d":0}

def collisionTrue(snakeCor, BombCor, padding):
    pass
        
#----------GLOBAL----------#


#----------GAME LOOP----------#
def gameLoop(keyLog):
    # Board Setup
    screen.fill("white")
    grid = Grid(screen, "darkgrey")
    grid.drawGrid()

    # Bomb Setup
    bomb = Bomb(screen)
    bomb.spawnCircle(BOMB_CENTER)
    bomb.drawArrows(screen, ARROW_COMB_OBJECTS)

    # Snake Setup & Movement
    snake = Snake(screen)
    snake.handleKeyLog(keys, keyLog)
    snake.head(keyLog, SNAKE_COR)

    # Setup Hitbox
    #hitbox = Hitbox(BOMB_CENTER, screen)

    pygame.display.flip()
#----------GAME LOOP----------#



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    gameLoop(keyLog)

    dt = clock.tick(11) / 1000

pygame.quit()