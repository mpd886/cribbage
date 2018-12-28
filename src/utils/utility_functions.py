import logging


def print_hand(hand):
    logging.debug(" ".join([str(c) for c in hand]))