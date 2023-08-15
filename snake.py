import pygame
import random
from board import Grid

class Snake: 
    def __init__(self, surface):
        self.surface = surface
        grid = Grid(self.surface, "black")
        self.padding = grid.padding
        self.width = grid.width
        self.lineCount = grid.LINE_COUNT
        self.snakeCor = []
        self.corList = []

    def spawnCor(self):
        for i in range(self.lineCount):
            self.corList.append(i * self.surface.get_width()//self.lineCount)
        while len(self.snakeCor) <= 1:
            self.snakeCor.append(random.choice(self.corList[1:len(self.corList)-1]))
        return self.snakeCor

    def handleKeyLog(self, keys, keyLog):
        if keys[pygame.K_w] and keyLog["w"] < 1:
            keyLog["w"] += 1
            keyLog["a"] = 0
            keyLog["s"] = 0
            keyLog["d"] = 0
        if keys[pygame.K_s] and keyLog["s"] < 1:
            keyLog["s"] += 1
            keyLog["w"] = 0
            keyLog["a"] = 0
            keyLog["d"] = 0
        if keys[pygame.K_a] and keyLog["a"] < 1:
            keyLog["a"] += 1
            keyLog["w"] = 0
            keyLog["s"] = 0
            keyLog["d"] = 0
        if keys[pygame.K_d] and keyLog["d"] < 1: 
            keyLog["d"] += 1
            keyLog["w"] = 0
            keyLog["s"] = 0
            keyLog["a"] = 0

        
    def head(self, keyLog, snakeCor):
        head = pygame.Rect((snakeCor[0]+self.width, snakeCor[1]+self.width), (self.padding - self.width, self.padding - self.width))
        pygame.draw.rect(self.surface, "green", head)
        # Handle movement
        if keyLog["w"]:
            snakeCor[1] -= self.padding
        if keyLog["a"]:
            snakeCor[0] -= self.padding
        if keyLog["s"]:
            snakeCor[1] += self.padding
        if keyLog["d"]:
            snakeCor[0] += self.padding

            