import logging
from graphics import CribbageDisplay



if __name__ == "__main__":
    # initialize graphics
    # show menu start/quit
    # game loop:
    #   choose first dealer
    #   while human_points != 121 and computer_points != 121
    #       deal cards
    #       get crib cards
    #       get starter card
    #
    logging.basicConfig(level=logging.DEBUG)
    display = CribbageDisplay()
    display.run()
