import pygame
import random
from board import Grid
from apple import Apple

class Snake: 
    def __init__(self, surface):
        self.surface = surface
        grid = Grid(self.surface, "black")
        apple = Apple(self.surface)
        self.padding = grid.padding
        self.xValues = apple.xValues
        self.yValues = apple.yValues

    def spawnCor(self):
        return(random.choice(self.xValues), random.choice(self.yValues))

    def spawnHead(self, spawnCor):
        head = pygame.Rect((spawnCor), (self.padding, self.padding))
        pygame.draw.rect(self.surface, "green", head)
    
    def move(self, keys):
        if keys[pygame.K_w]:
            print("Direction: up")
        if keys[pygame.K_s]:
            print("Direction: down")
        if keys[pygame.K_a]:
            pass
        if keys[pygame.K_d]: 
            pass
