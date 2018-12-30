import unittest
from game.scorer import CribbageScorer
from cards import Card, HEARTS, CLUBS, SPADES, DIAMONDS


def generate_hand(cards):
    return [Card(c[0], c[1]) for c in cards]


class CribbageScorerTests(unittest.TestCase):

    def test_pairs(self):
        hand = generate_hand([(4, HEARTS), (2, CLUBS), (4, SPADES), (10, CLUBS)])
        flip = Card(8, "Clubs")
        scorer = CribbageScorer(hand, flip)
        self.assertEqual(2, scorer.get_points_for_pairs())

    def test_three_of_a_kind(self):
        hand = generate_hand([(4, HEARTS), (5, SPADES), (4, SPADES), (6, HEARTS)])
        flip = Card(4, DIAMONDS)
        self.assertEqual(6, CribbageScorer(hand, flip).get_points_for_pairs())

    def test_two_pairs(self):
        hand = generate_hand([(4, HEARTS), (5, SPADES), (5, SPADES), (6, HEARTS)])
        flip = Card(4, DIAMONDS)
        self.assertEqual(4, CribbageScorer(hand, flip).get_points_for_pairs())

    def test_three_card_run(self):
        hand = generate_hand([(10, CLUBS), (12, SPADES), (11, SPADES), (8, SPADES)])
        flip = Card(6, HEARTS)
        scorer = CribbageScorer(hand, flip)
        self.assertEqual(3, scorer.get_points_for_runs())

    def test_four_card_run(self):
        hand = generate_hand([(2, SPADES), (5, HEARTS), (4, CLUBS), (3, CLUBS)])
        flip = Card(10, DIAMONDS)
        self.assertEqual(4, CribbageScorer(hand, flip).get_points_for_runs())

    def test_four_card_flush(self):
        hand = generate_hand([(2, SPADES), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, HEARTS)
        self.assertEqual(4, CribbageScorer(hand, flip).get_points_for_flush())

    def test_five_card_flush(self):
        hand = generate_hand([(2, SPADES), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, SPADES)
        self.assertEqual(5, CribbageScorer(hand, flip).get_points_for_flush())

    def test_no_flush(self):
        hand = generate_hand([(2, HEARTS), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, SPADES)
        self.assertEqual(0, CribbageScorer(hand, flip).get_points_for_flush())

    def test_fifteens(self):
        hand = generate_hand([(4, HEARTS), (5, SPADES), (4, SPADES), (6, HEARTS)])
        flip = Card(4, DIAMONDS)
        self.assertEqual(6, CribbageScorer(hand, flip).get_points_for_fifteens())

    def test_fifteens_with_fives(self):
        hand = generate_hand([(5, HEARTS), (5, SPADES), (10, SPADES), (5, DIAMONDS)])
        flip = Card(5, CLUBS)
        self.assertEqual(16, CribbageScorer(hand, flip).get_points_for_fifteens())

    def test_zero_total_points(self):
        hand = generate_hand([(1, SPADES), (3, HEARTS), (8, CLUBS), (10, HEARTS)])
        flip = Card(13, DIAMONDS)
        self.assertEqual(0, CribbageScorer(hand, flip).tally_points())

    def test_max_points(self):
        hand = generate_hand([(5, SPADES), (11, HEARTS), (5, DIAMONDS), (5, CLUBS)])
        flip = Card(5, HEARTS)
        self.assertEqual(29, CribbageScorer(hand, flip).tally_points())

    def test_no_four_card_flush_for_crib(self):
        hand = generate_hand([(2, SPADES), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, HEARTS)
        self.assertEqual(0, CribbageScorer(hand, flip, True).get_points_for_flush())

    def test_no_four_card_flush_for_crib2(self):
        hand = generate_hand([(2, HEARTS), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, SPADES)
        self.assertEqual(0, CribbageScorer(hand, flip, True).get_points_for_flush())

    def test_five_card_flush_for_crib(self):
        hand = generate_hand([(2, SPADES), (3, SPADES), (4, SPADES), (5, SPADES)])
        flip = Card(10, SPADES)
        self.assertEqual(5, CribbageScorer(hand, flip, True).get_points_for_flush())

    def test_four_card_score(self):
        hand = generate_hand([(2, SPADES), (3, SPADES), (4, SPADES), (5, SPADES)])
        self.assertEqual(8, CribbageScorer(hand).tally_points())


if __name__ == '__main__':
    unittest.main()
