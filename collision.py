import pygame
from bomb import Bomb
from board import Grid
from snake import Snake

class Collide:
    def __init__(self, screen, keylog, LINE_DIR, bombCenter, snakeCor, posComb, circleHitbox):
        s = Snake(screen, bombCenter)
        b = Bomb(screen)
        self.dir = 0
        for i in posComb.keys():
            if posComb[i]:
                self.dir = posComb[i]
        self.directionTest = False
        self.collideTest = False
        self.head = s.returnHead(snakeCor)
        self.keylogObject = []
        self.keylogObject.append(keylog["s"])
        self.keylogObject.append(keylog["a"])
        self.keylogObject.append(keylog["w"])
        self.keylogObject.append(keylog["d"])
        #print("keylogObejct:", self.keylogObject, "keylogObject[arrowdir]: ", self.keylogObject[arrowDir], "arrowDir:", arrowDir)

    def checkDir(self, direction):
        if self.keylogObject[direction["dir"]]:
            return True
        else:
            return False
        if self.head.collidepoint(bombCenter) and self.keylogObject[self.dir] == 0:
            self.collideTest = True
            self.directionTest = False
        
        