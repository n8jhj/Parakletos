import Player
import Board
import Charactor
import pdb

class Game(object):
    def __init__(self, DISPSURF):
        self.surf = DISPSURF # display surface game will be drawing on
        self.board = Board.Board(self) # Board on which Game is played
        self.plyrs = [] # Players list
        self.state = 'meatState' # setupState or meatState
        self.chgState = False # whether the state has changed
        self.selection = None # current selection to be displayed in HUD
        self.setup()

    def setup(self):
        # Add Players and Charactors
        self.addPlayer(1)
        self.addChar(self.plyrs[0], 3, 0)
        self.plyrs[0].chars[0].paintLOS(1)

    def draw(self):
        self.board.draw() # draw board
        for i in range(len(self.plyrs)): # draw players
            self.plyrs[i].draw()

    def addPlayer(self, num):
        self.plyrs.append(Player.Player(self, 'Player ' + str(num)))

    def addChar(self, player, x, y):
        # Create a Charactor. Add it to self, player, and the board.
        newChar = Charactor.Charactor(player)
        player.addChar(newChar)
        self.board.addChar(newChar,x,y)

    def clickOnChar(Charactor):
        """
        if another Charactor is selected:
            if they're on the same team and in pair range:
                pair up!
                return
            if they're not on the same team and in attack range:
                attack!
                return
        select the clicked Charactor
        """

    def clickOnTile(Tile):
        """
        if a Charactor is selected and in move range:
            move that Charactor to the clicked Tile
        otherwise:
            display properties of the clicked Tile
        """

    def clickOnItem(Item):
        """
        if a Charactor is selected and in pickUp range:
            have that Charactor pickUp the Item
        """

    def clickOnPlayer(Player):
        """
        display the Player's stats
        """

    def clickOnNothing():
        """
        display name of the game in HUD
        """

    def keyPressUp(self):
        # handle UP key press
        self.plyrs[0].chars[0].move('ahead')

    def keyPressDown(self):
        # handle DOWN key press
        self.plyrs[0].chars[0].move('behind')

    def keyPressLeft(self):
        # handle LEFT key press
        self.plyrs[0].chars[0].turn('left')

    def keyPressRight(self):
        # handle RIGHT key press
        self.plyrs[0].chars[0].turn('right')

    def keyPressW(self):
        # handle W key press
        self.plyrs[0].chars[0].move('ahead')

    def keyPressS(self):
        # handle S key press
        self.plyrs[0].chars[0].move('behind')

    def keyPressA(self):
        # handle A key press
        self.plyrs[0].chars[0].move('left')

    def keyPressD(self):
        # handle D key press
        self.plyrs[0].chars[0].move('right')
