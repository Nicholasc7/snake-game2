import pygame
# 900 x 900

class Grid:
    def __init__(self, surface, color):
        self.LINE_COUNT = 15
        self.surface = surface
        self.color = color
        self.padding = int(surface.get_width() / self.LINE_COUNT)

    
    def drawGrid(self):
        for i in range(self.LINE_COUNT + 1):
            # Vertical Lines
            pygame.draw.line(self.surface, self.color, (i * int(self.surface.get_width() / self.LINE_COUNT), 0), (i * int(self.surface.get_width() / self.LINE_COUNT),self.surface.get_width()), width = 1)

            # Horizontal Lines
            pygame.draw.line(self.surface, self.color, (0, i * int(self.surface.get_height() / self.LINE_COUNT)), (self.surface.get_width(), i * int(self.surface.get_height() / self.LINE_COUNT)), width = 1)

