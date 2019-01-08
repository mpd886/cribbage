import sys
import logging
from graphics import GraphicsObject, GameIntro
from game import game_state


def main():
    graphics = GraphicsObject()
    state = game_state.GAME_STATE_INTRO
    while True:
        if state == game_state.GAME_STATE_INTRO:
            state = GameIntro(graphics).run()
        elif state == game_state.GAME_STATE_PLAY:
            pass
        elif state == game_state.GAME_STATE_QUIT:
            logging.debug("QUITTING")
            sys.exit(0)
        else:
            logging.error(f"Unknown game state {state}")
            state = game_state.GAME_STATE_INTRO


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
    logging.basicConfig(level=logging.DEBUG, filename="cribbage.log")
    main()
