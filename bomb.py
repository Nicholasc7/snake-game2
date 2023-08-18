import pygame
import random
from board import Grid

class Bomb:
    def __init__(self,surface):
        self.surface = surface
        grid = Grid(self.surface, "black")
        lineCount = grid.LINE_COUNT
        self.width = grid.width
        self.padding = grid.padding
        self.xValues = []
        self.yValues = []
        # Gather X Values
        for i in range(lineCount):
            self.xValues.append(int(i * self.surface.get_width() / lineCount))
        # Gather Y Values
        for i in range(lineCount):
            self.yValues.append(int(i * self.surface.get_height() / lineCount))
        # Create all possible directions the bomb arrows can face
        self.possibleCombinations = [0, 1, 2, 3] #[up, right, down, left]

        

    # Find random center for Bomb spawn
    def findCenter(self):
        return [random.choice(self.xValues[1:len(self.xValues)-1]) + self.padding//2,random.choice(self.xValues[1:len(self.xValues)-1]) + self.padding//2]

    def spawnCircle(self, bombCenter):
        pygame.draw.circle(self.surface, "red", (bombCenter[0],bombCenter[1]), self.padding/3)
    
    def returnCircleHitbox(self, bombCenter):
        circleHitbox =  pygame.Rect((bombCenter[0] - self.padding/8,bombCenter[1] - self.padding/8), (self.padding/4, self.padding/4))
        return circleHitbox
        
    def drawUpdatedArrows(self, screen, arrowCombs, arrowDir):
        for i in range(4):
            if i == arrowDir:
                pygame.draw.rect(screen, 'blue', arrowCombs[i]) 
    
    def returnDir(self):
        return random.choice(self.possibleCombinations)