#C://Python27/python.exe

import pygame
import sys

# set up pygame
# set up Clock
game = Game() # set up Game

going = True

def main():
    while going:
        controllerTick()
        viewTick()
        # clock tick()

def controllerTick():
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            going = False
        if event.type == MOUSEBUTTONDOWN:
            what was clicked on?
            do actions corresponding to what was clicked on
    """

def viewTick():
    """
    board.draw()
    pygame.display.update(Rect) things in game.toDraw
    """

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
        sys.exit()

# END
