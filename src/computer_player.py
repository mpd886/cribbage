import utils
from scorer import CribbageScorer
from cards import cards_to_string


class ComputerPlayer:
    def __init__(self):
        self.hand = None
        self.is_dealer = False

    def deal(self, hand, is_dealer):
        """
        Give player their hand
        :param hand: list of 6 cards
        :param is_dealer: True if the player is the dealer
        """
        self.hand = hand
        self.is_dealer = is_dealer

    def get_crib_cards(self):
        """
        :return: two cards that go into crib
        """
        four_card_hands = utils.get_subsequences(self.hand, 4)
        scores = [(CribbageScorer(h).tally_points(), h) for h in four_card_hands]
        scores = sorted(scores, key=lambda x: x[0], reverse=True)
        for p in scores:
            print("{}: {}".format(p[0], cards_to_string(p[1])))
        return []
