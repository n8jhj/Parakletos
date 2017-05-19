import sp. abilities file

class Charactor(Piece):
    def __init__():
        """
        PROPERTIES:
        hea
        atk
        rng
        vis
        spd = 2 (default)
        spAbility: string name of special ability - default charge: move and
            attack in one go.
        trait: Trait attached to this Charactor
        plyr: Player self belongs to
        loc: current location of self
        pastLocs: list of last 3 turn's locations
        items: list of Items self is carrying
        stunned: int denoting how many turns of stun self has left
        pairChar: Charactor self is paired to (for trait sharing)
        active: whether the Charactor is still active in the present turn
        """

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

    def move(x,y):
        """
        if Tile at (x,y) moveable and in move range of self:
            add new location to end of locs list and move all other elements
                down an index. Use a generator (yield keyword) to do this.
            set the moved-to Tile's moveable to False.
            add self to Piece.Board's list of objects to be redrawn.
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
