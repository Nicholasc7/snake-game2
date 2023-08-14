import pygame
import random
from board import Grid

class Apple:
    def __init__(self,surface):
        self.surface = surface
        grid = Grid(self.surface, "black")
        lineCount = grid.LINE_COUNT
        self.padding = grid.padding
        self.xValues = []
        self.yValues = []

        # Gather X Values
        for i in range(lineCount):
            self.xValues.append(int(i * self.surface.get_width() / lineCount))
        
        # Gather Y Values
        for i in range(lineCount):
            self.yValues.append(int(i * self.surface.get_height() / lineCount))

    # Find random center for apple spawn
    def findCenter(self):
        return ((random.choice(self.xValues) + self.padding/2, random.choice(self.yValues) + self.padding/2))

    def spawnApple(self, center):
        pygame.draw.circle(self.surface, "blue", center, self.padding/3)