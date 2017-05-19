class Game(object):
    def __init__():
        """
        PROPERTIES:
        surf: display surface game will be drawing on
        state: state that the game is in: setupState or meatState
        chgState: whether the state has changed
        Players list
        Board
        Items list
        Charactors list
        selection: current selection to be displayed in HUD
        toDraw: list of things to be redrawn
        """

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
