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
direction = {"dir":0}
count = 0
randomBombSpawn = []
tileSize = screen.get_width() // grid.LINE_COUNT
for i in range(grid.LINE_COUNT):
    if i > 0:
        randomBombSpawn.append(tileSize*i - grid.padding//2)

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

# Snake initialize
s1 = Snake(screen, BOMB_CENTER)
SNAKE_COR = s1.spawnCor()
keyLog = {"w":0, "d":0, "s":0, "a":0}
        
#----------GLOBAL----------#


# TODO: Fix bomb line so it moves with the circle on collision, line isn't spawning at updated BOMB_CENTER or the BOMB_CENTER isn't updating


#----------GAME LOOP----------#
def gameLoop(keyLog, BOMB_CENTER, LINE_DIR, direction):
    # Board Setup
    screen.fill("white")
    grid = Grid(screen, "darkgrey")
    grid.drawGrid()

    # Bomb Setup
    bomb = Bomb(screen)
    bomb.spawnCircle(BOMB_CENTER)
    circleHitbox = bomb.returnCircleHitbox(BOMB_CENTER)
    pygame.draw.rect(screen, 'darkred', circleHitbox,12,8,8,8,8)

    for i in possibleCombinations.keys():
        if possibleCombinations[0]:
            up = pygame.Rect((BOMB_CENTER[0] - padding//3, BOMB_CENTER[1] - padding//2), (padding//3*2, padding//13))
            pygame.draw.rect(screen, 'blue', up)
            direction["dir"] = 0
            
        if possibleCombinations[1]:
            right = pygame.Rect((BOMB_CENTER[0] + padding//2 - grid.width*2, BOMB_CENTER[1] - padding//3), (padding//13, padding//3*2))
            pygame.draw.rect(screen, 'blue', right)
            direction["dir"] = 1

        if possibleCombinations[2]:
            down = pygame.Rect((BOMB_CENTER[0] - padding//3, BOMB_CENTER[1] + padding//2 - grid.width*2), (padding//3*2, padding//13))
            pygame.draw.rect(screen, 'blue', down)
            direction["dir"] = 2

        if possibleCombinations[3]:
            left = pygame.Rect((BOMB_CENTER[0] - padding//2, BOMB_CENTER[1] - padding//3), (padding//13, padding//3*2))
            pygame.draw.rect(screen, 'blue', left)
            direction["dir"] = 3



    # Snake Setup & Movement
    snake = Snake(screen, BOMB_CENTER)
    snake.handleKeyLog(keys, keyLog)
    snake.head(keyLog, SNAKE_COR)
    snakeHead = snake.returnHead(SNAKE_COR)

    # Handle Collision
    col = Collide(screen, keyLog, LINE_DIR, BOMB_CENTER, SNAKE_COR, possibleCombinations, circleHitbox)
    dirTest = col.checkDir(direction)
    #print("dirTest: ", dirTest)
    if pygame.Rect.colliderect(snakeHead, circleHitbox) and dirTest:
        BOMB_CENTER[1] = random.choice(randomBombSpawn[1:-1])
        BOMB_CENTER[0] = random.choice(randomBombSpawn[1:-1])
        print(randomBombSpawn)
        print(BOMB_CENTER)

        # If collision remove value from current direction
        for i in possibleCombinations.keys():
            if possibleCombinations[i]:
                possibleCombinations[i] -= 1
        # Add new value to random direction(key)
        i = random.choice(range(4))
        possibleCombinations[i] =+ 1
        # Equal LINE_DIR to the line direction
        for i in possibleCombinations.keys():
            if possibleCombinations[i]:
                direction["dir"] = i

        
    if col.collideTest and col.directionTest == 0:
        print("Lost Health!")
    pygame.display.flip()
#----------GAME LOOP----------#

#TODO: Spawn bomb at random location upon collision
#TODO: Spawn at least 1 grid tile away from border (no spawning on edge)
#TODO: Check for snake head AND body location so bomb doesn't spawn on top

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    gameLoop(keyLog, BOMB_CENTER, LINE_DIR, direction)

    dt = clock.tick(13) / 1000

pygame.quit()