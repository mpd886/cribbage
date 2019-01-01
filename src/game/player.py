

class HumanPlayer:
    def __init__(self):
        self.hand = None
        self.is_dealer = False

    def deal(self, hand, is_dealer):
        self.hand = sorted(hand)
        self.is_dealer = is_dealer

    def get_cards(self):
        return self.hand
