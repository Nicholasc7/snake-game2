import pygame
from bomb import Bomb
from board import Grid

class Hitbox:
    def __init__(self, bombCenter, screen):
        self.surface = screen
        self.gridInst = Grid(self.surface, 'black')
        self.padding = self.gridInst.padding
        self.hitbox = pygame.Rect((bombCenter[0] - self.padding/2, bombCenter[1] - self.padding/2), (self.padding/4, self.padding/4))
        #pygame.draw.rect(screen, 'blue', self.hitbox, 20, 300, 50, 50, 50)