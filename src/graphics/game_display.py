import os
import pygame
import graphics.graphics_utils as gutils
from graphics.display_object import DisplayObject
from game.game_manager import Cribbage
from utils import Point
from cards import Card, DIAMONDS


class GameDisplay(DisplayObject):
    CARD_HEIGHT = 300
    CARD_WIDTH = 200
    """
    This is the main game loop/display.
    """
    def __init__(self, parent):
        """
        :param parent: parent surface on which to draw
        """
        super().__init__(parent)
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
        self.game.update()
        return False

    def draw(self):
        rect = self.parent.get_rect()
        center = Point(rect.width/2, rect.height/2)
        self.draw_card(self.card_back, Card(1, DIAMONDS, 300, center.y))

        # draw computer's cards
        pc_hand = self.game.get_computer_cards()
        OVERLAP = 60 # how much should cards overlap when drawn
        y = 30 + GameDisplay.CARD_HEIGHT/2
        x = center.x - ((GameDisplay.CARD_WIDTH + len(pc_hand)*OVERLAP) / 2)
        for card in pc_hand:
            card.pos = Point(x, y)
            self.draw_card(self.card_back, card)
            x += OVERLAP

        hand = self.game.get_human_cards()
        y = rect.height - 30 - GameDisplay.CARD_HEIGHT/2
        x = center.x - ((GameDisplay.CARD_WIDTH + len(pc_hand)*OVERLAP) / 2)
        for card in hand:
            card.pos = Point(x, y)
            image = self.card_images[str(card)]
            self.draw_card(image, card)
            x += OVERLAP

        self.draw_crib()

    def draw_crib(self):
        rect = self.parent.get_rect()
        center = Point(rect.width/2, rect.height/2)
        OVERLAP = 10
        x = rect.width-400
        y = center.y
        for c in self.game.crib:
            self.draw_card(self.card_back, Card(1, DIAMONDS, x, y))
            x += OVERLAP

    def draw_card(self, card_image, card):
        """Draw a card centered on the center_point
        """
        top = card.pos.y - card_image.get_rect().height/2
        left = card.pos.x - card_image.get_rect().width/2
        self.parent.blit(card_image, (left, top))
