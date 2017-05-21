import pygame, sys, Game # First 3 lines are #temporary
import pygame
from pygame.locals import *
import ConfigParser
from Tile import Tile
import pdb

class Board(object):
    def __init__(self, game, layoutFile='test_level.txt'):
        self.game = game # Game self is in
        self.surf = game.surf # display surface to draw on
        self.layoutFile = layoutFile # file containing map information
        self.tiles = [] # list of Tiles indexed by grid location
        self.chars = [] # list of Charactors
        self.width = 0
        self.height = 0
        self.xStart = 25
        self.yStart = 25
        self.tw = 40 # tile width (pixels)
        self.th = 40 # tile height (pixels)
        self.changed = True # whether self needs to be redrawn
        self.setup()

    def setup(self):
        # look into self.layoutFile and load the proper Tiles
        levelMap = []
        levelKey = {}
        parser = ConfigParser.ConfigParser()
        parser.read(self.layoutFile)
        levelMap = parser.get('level', 'map').split('\n')
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                levelKey[section] = desc
        self.width = len(levelMap[0]) # 10
        self.height = len(levelMap) # 6
        self.tiles = [None]*self.width*self.height
        for i in range(self.height):
            for j in range(self.width):
                sym = levelMap[i][j]
                name = levelKey[sym]['name']
                img = levelKey[sym]['img']
                imgVis = levelKey[sym]['img_vis']
                mvbl = levelKey[sym]['moveable']
                mvbl = mvbl == 'True' or mvbl == 'true' or mvbl == '1' \
                       or mvbl == 'Yes' or mvbl == 'yes'
                sebl = levelKey[sym]['seeable']
                sebl = sebl == 'True' or sebl == 'true' or sebl == '1' \
                       or sebl == 'Yes' or sebl == 'yes'
                self.tiles[i*self.width+j] = Tile(self, (j,self.height-i-1), \
                                                  name, img, imgVis, mvbl, sebl)

    def draw(self):
        if self.changed:
            rect = pygame.Rect(self.xStart, self.yStart, \
                               self.width*self.tw, self.height*self.th)
            # loop through all Tiles, Charactors and draw them
            for i in range(self.height):
                for j in range(self.width):
                    tile = self.tiles[i*self.width+j]
                    tile.draw()
            for i in range(len(self.chars)):
                self.chars[i].draw()
            pygame.display.update(rect)
            self.changed = False

    def getTile(self, x, y):
        # Convert from bottom-left-oriented to top-left-oriented coordinates
        y_tLOCoords = self.height-1-y
        return self.tiles[y_tLOCoords * self.width + x]

    def addChar(self, char, x, y):
        # Adds Charactor char to the given (x,y) board position
        tile = self.getTile(x,y)
        tile.addChar(char)
        self.chars.append(char)
        char.updateLOS()

def main(): #temporary
    SIZE = (750, 400)
    DISPSURF = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Board test')
    pygame.init()
    FPS = 1
    fpsClock = pygame.time.Clock()
    game = Game.Game(DISPSURF)
    
    going = True
    while going:
        # EVENTS
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
        # DRAWING
        game.board.draw()
        # CLOCK
        fpsClock.tick(FPS)

if __name__ == '__main__': #temporary
    try:
        main()
    finally:
        pygame.quit()
        sys.exit()
