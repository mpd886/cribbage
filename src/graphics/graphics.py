import sys
from utils import Point
from .graphics_utils import *
from .opening import CardSwirlAnimation


class CribbageDisplay:
    def __init__(self):
        self.screen = None
        self._initialize()
        self.stop_animation = False

    def _initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def center(self):
        """
        Return a Point (object with x, y fields) that is the center of the display area
        :return:
        """
        rect = self.screen.get_rect()
        return Point(int(rect.width/2), int(rect.height/2))

    def update(self, game_manager):
        """
        Draws the screen
        :param game_manager: cribbage game manager
        :return:
        """
        pass

    def _check_input(self):
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_q:
                    sys.exit(0)

    def run(self):
        clock = pygame.time.Clock()
        animation = CardSwirlAnimation(self.screen)
        while True:
            elapsed = clock.tick(40)
            animation.update(elapsed)
            self.screen.fill(COLOR_BLACK, self.screen.get_rect())
            animation.draw()
            pygame.display.flip()
            self._check_input()
