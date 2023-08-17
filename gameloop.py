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
# Initialize dict with keys as directions and values as true or false
# Update the value of a key(direction) at random
# Assign LINE_DIR to the True key
possibleCombinations = {0:0, 1:0, 2:0, 3:0}
i = random.choice(range(4))
possibleCombinations[i] += 1
for i in possibleCombinations.keys():
    if possibleCombinations[i]:
        LINE_DIR = i
print(possibleCombinations)
print(LINE_DIR)

# Snake initialize
s1 = Snake(screen, BOMB_CENTER)
SNAKE_COR = s1.spawnCor()
keyLog = {"w":0, "d":0, "s":0, "a":0}
        
#----------GLOBAL----------#


# TODO: Fix bomb line so it moves with the circle on collision, line isn't spawning at updated BOMB_CENTER or the BOMB_CENTER isn't updating


#----------GAME LOOP----------#
def gameLoop(keyLog, BOMB_CENTER, LINE_DIR):
    # Board Setup
    screen.fill("white")
    grid = Grid(screen, "darkgrey")
    grid.drawGrid()

    # Bomb Setup
    bomb = Bomb(screen)
    bomb.spawnCircle(BOMB_CENTER)

    for i in possibleCombinations.keys():
        if possibleCombinations[0]:
            up = pygame.Rect((BOMB_CENTER[0] - padding//3, BOMB_CENTER[1] - padding//2), (padding//3*2, padding//13))
            pygame.draw.rect(screen, 'blue', up)
            
        if possibleCombinations[1]:
            right = pygame.Rect((BOMB_CENTER[0] + padding//2 - grid.width*2, BOMB_CENTER[1] - padding//3), (padding//13, padding//3*2))
            pygame.draw.rect(screen, 'blue', right)

        if possibleCombinations[2]:
            down = pygame.Rect((BOMB_CENTER[0] - padding//3, BOMB_CENTER[1] + padding//2 - grid.width*2), (padding//3*2, padding//13))
            pygame.draw.rect(screen, 'blue', down)

        if possibleCombinations[3]:
            left = pygame.Rect((BOMB_CENTER[0] - padding//2, BOMB_CENTER[1] - padding//3), (padding//13, padding//3*2))
            pygame.draw.rect(screen, 'blue', left)



    # Snake Setup & Movement
    snake = Snake(screen, BOMB_CENTER)
    snake.handleKeyLog(keys, keyLog)
    snake.head(keyLog, SNAKE_COR)

    # Handle Collision
    col = Collide(screen, keyLog, LINE_DIR, BOMB_CENTER, SNAKE_COR, possibleCombinations)
    if col.collideTest and col.directionTest:
        BOMB_CENTER[1] += 80
        BOMB_CENTER[0] += 80
        # If collision remove value from current direction
        for i in possibleCombinations.keys():
            if possibleCombinations[i]:
                possibleCombinations[i] -= 1
        # Add new value to random direction(key)
        i = random.choice(range(4))
        possibleCombinations[i] =+ 1
        
        
    if col.collideTest and col.directionTest == 0:
        print("Lost Health!")

    pygame.display.flip()
#----------GAME LOOP----------#

#TODO: collision test isnt updating the direction of the line, keeping only the initial direction. Maybe store in dict?

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    gameLoop(keyLog, BOMB_CENTER, LINE_DIR)

    dt = clock.tick(10) / 1000

pygame.quit()