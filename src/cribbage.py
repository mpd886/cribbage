import random
import logging
import utils


JACK = 11
QUEEN = 12
KING = 13


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

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
        face_cards = {11: 'J', 12: 'Q', 13: 'K'}
        if self.rank <= 10:
            return f'{self.rank}{self.suit[0]}'
        else:
            return f'{face_cards[self.rank]}{self.suit[0]}'

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


def deal_hand(deck):
    return [deck.draw() for c in range(4)]


def print_hand(hand):
    logging.debug(" ".join([str(c) for c in hand]))


class CribbageScorer:
    def __init__(self, hand, flip_card=None, is_crib=False):
        self.hand = hand.copy()
        self.flip = flip_card
        self.is_crib = is_crib
        self.all_cards = hand.copy()
        if self.flip is not None:
            self.all_cards.append(self.flip)
        self.runs = {}
        self.all_sequences = None

    def _init_analysis(self):
        if self.all_sequences is not None:
            return

        self.all_sequences = []
        for x in range(2, 6):
            self.all_sequences.extend(utils.get_subsequences(self.all_cards, x))

    @staticmethod
    def sum_cards(cards):
        total = 0
        for c in cards:
            total += c.val
        return total

    @staticmethod
    def is_sequence(cards):
        i = 0
        j = 1
        while j < len(cards):
            if cards[i].rank != cards[j].rank-1:
                return False
            i += 1
            j += 1
        return True

    def _add_run(self, run):
        cardset = set(run)

        test_runs = self.runs.setdefault(len(run)+1, [])
        for r in test_runs:
            if cardset.issubset(r):
                return
        self.runs.setdefault(len(run), []).append(cardset)

    def get_points_for_runs(self):
        self._init_analysis()

        reorderd = sorted(self.all_sequences, key=len, reverse=True)
        points = 0
        for s in reorderd:
            if len(s) >= 3 and CribbageScorer.is_sequence(s):
                self._add_run(s)
        for runs in self.runs.values():
            for run in runs:
                points += len(run)
                print_hand(run)
        return points

    def get_points_for_flush(self):
        suits = set(map(lambda x: x.suit, self.hand))
        if len(suits) == 1:
            if self.flip is not None and suits.pop() == self.flip.suit:
                return 5
            elif not self.is_crib:
                return 4
            else:
                return 0
        else:
            return 0

    def get_points_for_fifteens(self):
        self._init_analysis()
        points = 0
        for s in self.all_sequences:
            if CribbageScorer.sum_cards(s) == 15:
                points += 2
        return points

    def get_points_for_pairs(self):
        self._init_analysis()
        points = 0
        for s in self.all_sequences:
            if len(s) == 2 and s[0].rank == s[1].rank:
                points += 2
        return points

    def get_points_for_nobs(self):
        if self.flip is None:
            return 0

        for c in self.hand:
            if c.rank == JACK and c.suit == self.flip.suit:
                return 1
        return 0

    def tally_points(self):
        points = 0
        points += self.get_points_for_fifteens()
        points += self.get_points_for_flush()
        points += self.get_points_for_pairs()
        points += self.get_points_for_runs()
        points += self.get_points_for_nobs()
        return points
