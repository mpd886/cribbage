import logging
from cards import Deck
from computer_player import ComputerPlayer
from player import HumanPlayer
from graphics import CribbageDisplay


class Cribbage:
    HUMAN = "human"
    COMPUTER = "computer"

    def __init__(self):
        self.deck = None
        self.starter = None
        self.board = None
        self.players = {Cribbage.HUMAN: HumanPlayer(),
                        Cribbage.COMPUTER: ComputerPlayer()}

    def play(self):
        self.deck = Deck()
        self.board = {Cribbage.HUMAN: 0,
                      Cribbage.COMPUTER: 0}

        #


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
