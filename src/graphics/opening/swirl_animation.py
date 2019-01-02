import pygame
import os
import math
import random
from graphics import graphics_utils as gutils
from graphics.display_object import DisplayObject
from utils import Point


SWIRL_SPEED = 0.2
CIRCLE_RADIUS = 0.5
SWIRL_GROW_SPEED = 0.1


class MovingCard:
    def __init__(self, card, x, y):
        self.x = x
        self.y = y
        self.card = card
        self.theta_degrees = 0
        self.swirl_size = CIRCLE_RADIUS
        self.growth_direction = 1

    def update(self, elapsed_time):
        self.theta_degrees = (self.theta_degrees + elapsed_time * SWIRL_SPEED) % 360
        radians = math.radians(self.theta_degrees)
        self.x += math.sin(radians) * self.swirl_size
        self.y += math.cos(radians) * self.swirl_size
        self.swirl_size += SWIRL_GROW_SPEED*self.growth_direction
        if self.swirl_size >= 50 or self.swirl_size <= 0:
            self.growth_direction = -self.growth_direction


class CardSwirlAnimation(DisplayObject):
    """
    This animation shows cards "flying" off the deck into a swirl shape.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.images = gutils.load_card_images(gutils.IMAGES_BASE_DIRECTORY, (100, 150))
        random.shuffle(self.images)
        self.back = pygame.image.load(os.path.join(gutils.IMAGES_BASE_DIRECTORY, gutils.CARD_BACK_IMAGE))
        self.back = pygame.transform.scale(self.back, (100, 150))
        self.moving = [] # list of moving cards
        self.card_delay = 0

    def update(self, elapsed_time):
        """
        Update the animation
        :param parent: surface on which we are drawing
        :param elapsed_time: elapsed time (ms)
        :return: return True if done
        """
        self.card_delay += elapsed_time
        for card in self.moving:
            card.update(elapsed_time)
        if self.card_delay > 100 and len(self.images):
            card = self.images.pop()
            self._init_card(card)
            self.card_delay = 0
        return False

    def draw(self):
        if len(self.images) > 0:
            self.parent.blit(self.back, self._get_deck_position())
        for card in self.moving:
            self.parent.blit(card.card, (card.x, card.y))

    def _init_card(self, card):
        deck_pos = self._get_deck_position()
        self.moving.insert(0, MovingCard(card, deck_pos.x + 10, deck_pos.y))

    def _get_deck_position(self):
        """
        Return Point of where the deck starts
        :return:
        """
        rect = self.parent.get_rect()
        x = rect.width/2
        y = rect.height/2
        return Point(x+10, y)
