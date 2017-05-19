#C://Python27/python.exe

"""
PARAKLETOS

A game where players take turns advancing towards each other's bases until
one team takes the other's flag.
"""

# __________________________79_CHARACTERS______________________________________


import pygame, sys
from pygame.locals import *
from Colors import *
import Game

# set up pygame
SIZE = (750, 400)
DISPSURF = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Parakletos')
pygame.init()

# set up Clock
FPS = 30
fpsClock = pygame.time.Clock()

# set up Game
game = Game.Game(DISPSURF)

def main():
    going = True
    
    while going:
        going = controllerTick() # event handling
        viewTick() # drawing
        fpsClock.tick(FPS) # clock

def controllerTick():
    for event in pygame.event.get():
        if event.type == QUIT:
            return False
        if event.type == MOUSEBUTTONDOWN:
            # what was clicked on?
            # do actions corresponding to what was clicked on
            pass
        if event.type == KEYDOWN:
            # Put this all into a dictionary in Game.py
            if event.key == K_UP:
                game.keyPressUp()
            elif event.key == K_DOWN:
                game.keyPressDown()
            elif event.key == K_LEFT:
                game.keyPressLeft()
            elif event.key == K_RIGHT:
                game.keyPressRight()
            elif event.key == K_w:
                game.keyPressW()
            elif event.key == K_s:
                game.keyPressS()
            elif event.key == K_a:
                game.keyPressA()
            elif event.key == K_d:
                game.keyPressD()
    return True

def viewTick():
    game.draw()
    pass

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        # sys.exit() #temporary

# END
