class Piece(object):
    def __init__(self, holder): # holder will be Tile, Charactor, or Player
        self.holder = holder

    def getLoc(self):
        return self.holder.loc

    def move(x,y):
        """
        location = (x,y)
        add self to Board's list of objects to be redrawn
        """
        pass
