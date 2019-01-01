import os
import pygame
import graphics.graphics_utils as gutils
from game.game_manager import Cribbage
from utils import Point


class GameDisplay:
    CARD_HEIGHT = 300
    CARD_WIDTH = 200
    """
    This is the main game loop/display.
    """
    def __init__(self, parent):
        """
        :param parent: parent surface on which to draw
        """
        self.parent = parent
        self.game = Cribbage()
        self.game.play()
        self.card_back = GameDisplay.load_image(os.path.join(gutils.IMAGES_BASE_DIRECTORY, gutils.CARD_BACK_IMAGE))
        self.card_images = self._load_cards()

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
        rect = self.parent.get_rect()
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

    def draw_card(self, card, center_point):
        """Draw a card centered on the center_point
        """
        top = center_point.y - card.get_rect().height/2
        left = center_point.x - card.get_rect().width/2
        self.parent.blit(card, (left, top))
