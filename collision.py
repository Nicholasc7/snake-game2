import pygame
from bomb import Bomb
from board import Grid
from snake import Snake

class Collide:
    def __init__(self, screen, keylog, arrowDir, bombCenter, snakeCor):
        s = Snake(screen, bombCenter)
        b = Bomb(screen)
        self.validDirection = False
        self.collide = False
        self.head = s.returnHead(snakeCor)
        self.keylogObject = []
        self.keylogObject.append(keylog["s"])
        self.keylogObject.append(keylog["a"])
        self.keylogObject.append(keylog["w"])
        self.keylogObject.append(keylog["d"])
        #print("keylogObejct:", self.keylogObject, "arrowDir:", arrowDir)

        if self.head.collidepoint(bombCenter) and self.keylogObject[arrowDir]:
            self.collide = True
            arrowCombinations = b.returnArrowCombObjects
            bombCenter[0] += 100
