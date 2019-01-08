import os
import pygame
import graphics.graphics_utils as gutils
from game.game_manager import Cribbage
from utils import Point
from game import game_state


class GameDisplay:
    CARD_HEIGHT = 300
    CARD_WIDTH = 200
    """
    This is the main game loop/display.
    """
    def __init__(self, graphics):
        """
        :param parent: parent surface on which to draw
        """
        self.graphics = graphics
        self.game = Cribbage()
        self.game.play()
        self.card_back = GameDisplay.load_image(os.path.join(gutils.IMAGES_BASE_DIRECTORY, gutils.CARD_BACK_IMAGE))
        self.card_images = self._load_cards()
        self.keep_going = True
        self.state = None

    def _load_cards(self):
        images = {}
        for c in os.listdir(gutils.IMAGES_BASE_DIRECTORY):
            fp = os.path.join(gutils.IMAGES_BASE_DIRECTORY, c)
            if not os.path.isdir(fp):
                image = GameDisplay.load_image(fp)
                images[os.path.splitext(c)[0]] = image
        return images

    @staticmethod
    def load_image(path):
        image = pygame.image.load(path)
        return pygame.transform.scale(image, (GameDisplay.CARD_WIDTH, GameDisplay.CARD_HEIGHT))

    def update(self, elapsed_time):
        """
        :param elapsed_time: time since last call in ms
        :return: True if the display is done/exhausted/disposed
        """
        return False

    def draw(self):
        rect = self.graphics.get_rect()
        self.graphics.clear_screen(gutils.COLOR_DARK_GREEN)
        center = Point(rect.width/2, rect.height/2)
        self.draw_card(self.card_back, Point(300, center.y))

        # draw computer's cards
        pc_hand = self.game.get_computer_cards()
        OVERLAP = 60 # how much should cards overlap when drawn
        y = 30 + GameDisplay.CARD_HEIGHT/2
        x = center.x - ((GameDisplay.CARD_WIDTH + len(pc_hand)*OVERLAP) / 2)
        for card in pc_hand:
            self.draw_card(self.card_back, Point(x, y))
            x += OVERLAP

        hand = self.game.get_human_cards()
        y = rect.height - 30 - GameDisplay.CARD_HEIGHT/2
        x = center.x - ((GameDisplay.CARD_WIDTH + len(pc_hand)*OVERLAP) / 2)
        for card in hand:
            image = self.card_images[str(card)]
            self.draw_card(image, Point(x, y))
            x += OVERLAP

        self.graphics.flip()

    def draw_card(self, card, center_point):
        """Draw a card centered on the center_point
        """
        top = center_point.y - card.get_rect().height/2
        left = center_point.x - card.get_rect().width/2
        self.graphics.blit(card, (left, top))

    def run(self):
        while self.keep_going:
            self.draw()
            self.update(self.graphics.clock.tick(40))
            self.check_input()

        return self.state

    def check_input(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_q):
                self.state = game_state.GAME_STATE_QUIT
                self.keep_going = False
                return
