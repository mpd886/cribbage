import unittest
from cards import Card, HEARTS, CLUBS, SPADES, DIAMONDS
from computer_player import ComputerPlayer


class ComputerPlayerTet(unittest.TestCase):

    def test_discards(self):
        hand = [Card(1, HEARTS), Card(2, SPADES), Card(3, CLUBS),
                Card(10, DIAMONDS), Card(6, CLUBS), Card(7, CLUBS)]
        cp = ComputerPlayer()
        cp.deal(hand, False)

        crib_cards = cp.get_crib_cards()

        self.assertTrue(Card(6, CLUBS) in crib_cards)
        self.assertTrue(Card(7, CLUBS) in crib_cards)


if __name__ == '__main__':
    unittest.main()
