import sys
from utils import Point
from .graphics_utils import *
from .opening import CardSwirlAnimation


class CribbageDisplay:
    def __init__(self):
        self.screen = None
        self._initialize()
        # list of objects with update(elapsed_time) and draw() methods
        self.display_list = []

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

    def update(self, elapsed_time):
        """
        Draws the screen
        :param elapsed_time: milliseconds since the last time called
        :return:
        """
        for disp_obj in self.display_list:
            disp_obj.update(elapsed_time)

    def draw(self):
        self.screen.fill(COLOR_BLACK, self.screen.get_rect())
        for disp_obj in self.display_list:
            disp_obj.draw()
        pygame.display.flip()

    def _check_input(self):
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_q:
                    sys.exit(0)

    def run(self):
        clock = pygame.time.Clock()
        self.display_list.append(CardSwirlAnimation(self.screen))
        while True:
            elapsed = clock.tick(40)
            self.update(elapsed)
            self.draw()
            self._check_input()
