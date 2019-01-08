import random
from utils import Point


HEARTS = "Hearts"
CLUBS = "Clubs"
DIAMONDS = "Diamonds"
SPADES = "Spades"

JACK = 11
QUEEN = 12
KING = 13


class Card:
    def __init__(self, rank, suit, x=0, y=0):
        self.rank = rank
        self.suit = suit
        self.pos = Point(x, y)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit and other.suit

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __hash__(self):
        result = 17
        result = 31 * result + self.rank
        result = 31 * result + hash(self.suit)
        return result

    def __str__(self):
        face_cards = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        if self.rank in face_cards:
            return f'{face_cards[self.rank]}{self.suit[0]}'
        else:
            return f'{self.rank}{self.suit[0]}'

    @property
    def val(self):
        return self.rank if self.rank <= 10 else 10


class Deck:
    def __init__(self):
        self.cards = Deck.build_deck()

    def draw(self):
        return self.cards.pop()

    @staticmethod
    def build_deck():
        cards = [Card(r, s) for r in range(1, 13) for s in ["Club", "Diamond", "Heart", "Spade"]]
        random.shuffle(cards)
        return cards


def cards_to_string(hand):
    return " ".join([str(c) for c in hand])
