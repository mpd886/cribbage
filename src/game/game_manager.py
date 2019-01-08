from cards import Deck
from .computer_player import ComputerPlayer
from .player import HumanPlayer


GAME_STATE_DONE = 0
GAME_STATE_GET_CRIB = 1
GAME_STATE_PEGGING = 2
GAME_STATE_SCORING = 3


class Cribbage:
    HUMAN = "human"
    COMPUTER = "computer"

    def __init__(self):
        self.deck = None
        self.starter = None
        self.board = None
        self.players = {Cribbage.HUMAN: HumanPlayer(),
                        Cribbage.COMPUTER: ComputerPlayer()}
        self.crib = []
        self.game_state = GAME_STATE_DONE

    def play(self):
        self.deck = Deck()
        self.board = {Cribbage.HUMAN: 0,
                      Cribbage.COMPUTER: 0}
        self.players[Cribbage.COMPUTER].deal([self.deck.draw() for c in range(6)], False)
        self.players[Cribbage.HUMAN].deal([self.deck.draw() for c in range(6)], False)

    def get_computer_cards(self):
        return self.players[Cribbage.COMPUTER].get_cards()

    def get_human_cards(self):
        return self.players[Cribbage.HUMAN].get_cards()

    def update(self):
        pass

