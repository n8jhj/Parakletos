from pygame import image, display, Rect
import Charactor
import pdb

class Tile(object):
    def __init__(self, board, loc, name='ground', \
                 imgFile='sunset_gradient_oval', \
                 imgVisFile='sunset_gradient_oval2', moveable=True, \
                 seeable=True):
        self.board = board # Board self is in
        self.surf = board.surf
        self.loc = loc # grid location - (x,y)
        self.name = name # name of the type of self
        self.img = image.load(imgFile) # default image
        self.imgVis = image.load(imgVisFile) # image when visible
        self.currImg = self.img # current image representing self
        self.rect = self.getRect()
        self.moveable = moveable # whether Charactors can move here
        self.seeable = seeable # whether Charactors can see past here
        self.piece = None # Piece self contains
        self.changed = True # whether self needs to be redrawn

    def __repr__(self):
        return str(self.loc)

    def getRect(self):
        x = self.loc[0]
        y = self.board.height - self.loc[1] - 1
        rect = Rect(self.board.xStart+x*self.board.tw, \
                    self.board.yStart+y*self.board.th, \
                    self.board.tw, self.board.th)
        return rect

    # Draw self at pixel locations determined by rect
    def draw(self):
        if self.changed:
            self.surf.blit(self.currImg, (self.rect.x, self.rect.y))
            self.board.addToNewRects(self.rect)
            self.changed = False

    def getTileAdjacent(self, (dx,dy)):
        # Gets the tile dx units away in x, dy units away in y
        adjx = self.loc[0]+dx
        adjy = self.loc[1]+dy
        if adjx >= 0 and adjx <= self.board.width-1 \
           and adjy >= 0 and adjy <= self.board.height-1:
            return self.board.getTile(adjx, adjy)
        return None

    def addChar(self, char):
        assert self.piece == None, 'There\'s already a Piece on this Tile!'
        char.holder = self
        self.piece = char

    def inMoveRange(Charactor):
        # sthg like: return whether abs(delta-x) + abs(delta-y) <=
        #     Charactor.spd
        pass
