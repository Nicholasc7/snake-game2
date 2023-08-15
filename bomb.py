import pygame
import random
from board import Grid

class Bomb:
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
        # Create all possible directions the bomb arrows can face
        self.possibleCombinations = [0, 1, 2, 3] #[up, right, down, left]
        self.arrowCombinations = []

    # Find random center for Bomb spawn
    def findCenter(self):
        print(self.xValues)
        return [random.choice(self.xValues[1:len(self.xValues)-1]) + self.padding//2,random.choice(self.xValues[1:len(self.xValues)-1]) + self.padding//2]
        return [random.choice(self.xValues) + self.padding/2, random.choice(self.yValues) + self.padding/2]

    def spawnCircle(self, center):
        pygame.draw.circle(self.surface, "red", (center[0],center[1]), self.padding/3)
    
    def spawnDir(self, screen, bombCenter):
            direction = random.choice(self.possibleCombinations)
            for i in range(4):
                 if i == direction:
                      return direction
    
    def returnArrowCombObjects(self, screen, bombCenter, arrowDir):
        self.Up1 = pygame.Rect((bombCenter[0] - self.padding//2, bombCenter[1] - self.padding//2), (self.padding//4, self.padding//13))
        self.arrowCombinations.append(self.Up1)
        self.Up2 = pygame.Rect((bombCenter[0] + self.padding//2 - self.padding//4, bombCenter[1] - self.padding//2), (self.padding//4, self.padding//13))
        self.arrowCombinations.append(self.Up2)
        self.Up3 = pygame.Rect((bombCenter[0] - self.padding//2, bombCenter[1] - self.padding//2), (self.padding//13, self.padding//6))
        self.arrowCombinations.append(self.Up3)
        self.Up4 = pygame.Rect((bombCenter[0] - self.padding//2, bombCenter[1] - self.padding//2), (self.padding//13, self.padding//6))
        self.arrowCombinations.append(self.Up4)

        return self.arrowCombinations

        
    
    def drawArrows(self, screen, arrowCombs):
        pygame.draw.rect(screen, 'blue', arrowCombs[0], 10)

        pygame.draw.rect(screen, 'blue', arrowCombs[1])
        pygame.draw.rect(screen, 'blue', arrowCombs[2])
        