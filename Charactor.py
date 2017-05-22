from Piece import Piece
from pygame import image, display, transform, Rect
import pygame
import pdb
#import sp. abilities file

class Charactor(Piece):
    def __init__(self, holder):
        super(Charactor, self).__init__(holder)
        self.surf = holder.surf
        self.imgFile = 'char_test.png' # image to represent self on the screen
        self.img = image.load(self.imgFile)
        self.hea = 1 # health
        self.atk = 1 # attack
        self.rng = (1,0) # range - (melee attack, ranged attack)
        self.vis = 3 # vision
        self.spd = 2 # speed
        self.spAbility = None # special ability name
        self.trait = None # Trait name
        self.plyr = None # Player self belongs to
        self.pastLocs = [] # list of last 5 locations
        self.LOS = [None] * self.getNumLOSTiles() # list of Tiles in LOS
        self.wallInLOS = [None] * len(self.LOS) # list of wall Tiles in LOS
        self.items = [] # list of Items self is carrying
        self.dir = 0 # direction (measured in degrees CCW from straight up)
        self.stunned = 0 # int denoting how many turns of stun self has left
        self.pairChar = None # Charactor self is paired to (for trait sharing)
        self.active = 1 # whether self is still active in the present turn

    # In future, this should account for which Player's turn it is
    # (Don't draw if on the opposing Player's team and out of LOS)
    def draw(self):
        # draw icon
        rect = self.holder.rect
        x = rect.x + 2
        y = rect.y + 2
        drawImg = transform.rotate(self.img, self.dir)
        self.surf.blit(drawImg, (x,y))
        # draw LOS lines
        lx1, ly1 = 0, 0
        lx2, ly2 = 500, 500
        pygame.draw.line(self.surf, (255,0,0), (lx1,ly1), (lx2,ly2), 2)
        x = min(lx1,lx2)
        y = min(ly1,ly2)
        w = abs(lx2-lx1)
        h = abs(ly2-ly1)
        rect = Rect(x, y, w, h)

    def updateBoard(self):
        self.holder.board.changed = True

    def getNumLOSTiles(self):
        visCount = 0
        visCountGen = (i/2 for i in range(self.vis))
        for el in visCountGen:
            visCount += el
        return (3*self.vis) + (2*visCount) + 1

    def clearWallInLOS(self):
        self.wallInLOS = [None] * len(self.LOS)

    # updates self.LOS by overwriting it
    # order is from middle to outsides (i), near to far (j)
    def updateLOS(self):
        self.clearWallInLOS()
        currLoc = self.getLoc()
        count = 0
        wallCount = 0
        for i in range((self.vis+1)/2):
            for j in range(i, self.vis-i):
                if i == 0:
                    if j == 0:
                        # add Tile at self
                        count,wallCount = self.addLOSTile(count,wallCount, \
                                                             'ahead',j)
                    # add Tile j+1 ahead of self to LOS
                    count,wallCount = self.addLOSTile(count,wallCount, \
                                                         'ahead',j+1)
                # add Tile left by (i+1) and ahead by j to LOS
                count,wallCount = self.addLOSTile(count,wallCount, \
                                                     'left',i+1,'ahead',j)
                # add Tile right by (i+1) and ahead by j to LOS
                count,wallCount = self.addLOSTile(count,wallCount, \
                                                     'right',i+1,'ahead',j)

    def addLOSTile(self, cnt, wallCnt, *args):
        t = self.getTile(args)
        self.LOS[cnt] = t
        cnt += 1
        if not t == None and not t.seeable:
            self.wallInLOS[wallCnt] = t
            wallCnt += 1
        return (cnt,wallCnt)

    def paintLOS(self, on):
        for t in self.LOS:
            if not t == None:
                if on:
                    t.currImg = t.imgVis
                else:
                    t.currImg = t.img
        self.updateBoard()

    def move(self, direction):
        tileTo = self.getTile((direction,1)) # get Tile to be moved to
        if self.canMoveTo(tileTo):
            self.updatePastLocs()
            self.holder.piece = None
            tileTo.piece = self
            self.updateBoard() # board should be redrawn
            self.holder = tileTo
            self.paintLOS(0)
            self.updateLOS()
            self.paintLOS(1)

    def turn(self, direction):
        dirDict = {'left':90, 'right':-90} # direction dictionary definition
        self.dir = (self.dir + dirDict[direction]) % 360
        self.updateBoard() # board should be redrawn
        self.paintLOS(0)
        self.updateLOS()
        self.paintLOS(1)

    # get Tile certain number of spaces away. E.g.:
    # self.getTile(('ahead',2,'left',3)) gets Tile 2 ahead and 3 left from self
    # String options: 'ahead' 'behind' 'left' 'right'
    def getTile(self, pairs):
        assert len(pairs)%2==0, 'Must input even number of arguments'
        rotDict = {0:(0,1), 90:(-1,0), 180:(0,-1), 270:(1,0)} # rotation dict
        tlnDict = {'ahead':0, 'behind':180, 'right':270, 'left':90} \
                  # translation dict
        adjCoords = [0,0]
        for i in range(len(pairs)/2):
            n = pairs[i*2+1]
            tlnAngle = tlnDict[pairs[i*2]]
            rotAngle = self.dir
            effectRot = (tlnAngle + rotAngle) % 360 # effective rotation
            dirPair = rotDict[effectRot] # directional pair to add to adjCoords
            adjCoords[0] += dirPair[0] * n
            adjCoords[1] += dirPair[1] * n
        return self.holder.getTileAdjacent(adjCoords)

    # whether self can move to the given Tile
    def canMoveTo(self, tile):
        if tile == None: # tile doesn't exist
            return False
        if not tile.moveable: # tile is a wall
            return False
        if isinstance(tile.piece, Charactor): # there's a Charactor there
            return False
        return True # otherwise tile can be moved to

    def updatePastLocs(self):
        self.pastLocs.insert(0,self.getLoc())
        if len(self.pastLocs) > 5:
            del self.pastLocs[len(self.pastLocs)-1]

    def pickUp(Item):
        """
        Item.owner = self
        Item.available = False
        add Item to Piece.Board's list of objects to be redrawn - will be
            off Board (with Charactor self)
        active = False
        """

    def drop(Item):
        """
        Item.owner = None
        Item.available = True
        Item.location = self.location
        active = False
        """

    def spAbility():
        """
        use sp. ability by:
            1. Check if the correct flower is in self.items
            2. If so, delete it from items
            3. Use sp. ability: refer to file containing sp. ability fcns.
        active = False
        """

    def attack(Charactor):
        """
        Charactor.hea -= self.atk
        if Charactor.hea <= 0:
            Charactor.die()
        active = False
        """

    def die():
        """
        set self.loc = self.plyr.baseLoc
        set self.stun = 1 (1 turn of stun before able to move again)
        set self.pairChar.pairChar = None
        set self.pairChar = None
        add self to Piece.Board's list of objs to be drawn
        """

    def pair(Charactor):
        """
        self.pairChar = Charactor
        Charactor.pairChar = self
        active = False
        """
