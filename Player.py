class Player(object):
    def __init__(self, game, name=None):
        self.game = game # Game self is in
        self.surf = self.game.surf
        self.name = name # name of this Player
        self.statsFile = None # file containing Player's stats
        self.color = None # color of this Player's Charactors
        self.loc = None # used for Charactors not on the board yet
        self.baseLoc = None # (x,y) grid location of this Player's base
        self.chars = [] # list of Charactors this Player has
        self.setup()

    def setup(self):
        # This is where all this Player's attributes are set up
        pass

    def draw(self):
        pass

    def addChar(self, char):
        char.plyr = self
        self.chars.append(char)

    def delChar(self, ind):
        # Deletes the Charactor at ind and returns it
        return self.chars.pop(ind)

    def joinGame():
        """
        add self to self.game
        """

    def leaveGame():
        """
        add game stats to self.statsFile
        """
