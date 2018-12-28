import utils
import cards


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
    def sum_cards(hand):
        total = 0
        for c in hand:
            total += c.val
        return total

    @staticmethod
    def is_sequence(hand):
        i = 0
        j = 1
        while j < len(hand):
            if hand[i].rank != hand[j].rank-1:
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
                utils.print_hand(run)
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
            if c.rank == cards.JACK and c.suit == self.flip.suit:
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
