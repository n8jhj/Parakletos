class Piece(object):
    def __init__(holder (will be Tile or Charactor)):
        """
        PROPERTIES:
        if holder isInstanceOf(Tile):
            Board = Tile.Board
        elif holder isInstanceOf(Charactor):
            Board = Charactor.Tile.Board
        else:
            print 'Must initialize Piece with Tile or Charactor.'
        location: (x,y)
        """

    def move(x,y):
        """
        location = (x,y)
        add self to Board's list of objects to be redrawn
        """
