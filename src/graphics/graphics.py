import sys
from utils import Point
from .graphics_utils import *
from .opening import GameIntro
from .game_display import GameDisplay


GAME_STATE_OPENING = 1
GAME_STATE_CRIBBAGE = 2


class CribbageDisplay:
    def __init__(self):
        self.screen = None
        self._initialize()
        # list of objects with update(elapsed_time) and draw() methods
        self.display_list = []
        self.state = GAME_STATE_OPENING

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
        disposed = []
        for disp_obj in self.display_list:
            if disp_obj.update(elapsed_time):
                disposed.append(disp_obj)
        for d in disposed:
            self.display_list.remove(d)

    def draw(self):
        self.screen.fill(COLOR_DARK_GREEN, self.screen.get_rect())
        for disp_obj in self.display_list:
            disp_obj.draw()
        pygame.display.flip()

    def _check_input(self):
        for evt in pygame.event.get():
            if evt.type == pygame.KEYDOWN or evt.type == pygame.KEYUP:
                self._process_key_event(evt)
            elif evt.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
                self._process_mouse_event(evt)
            elif evt.type == pygame.QUIT:
                sys.exit(0)

    def _process_key_event(self, evt):
        for obj in self.display_list[::-1]:
            if obj.handle_key_event(evt):
                return

        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_q:
                sys.exit(0)
            elif evt.key == pygame.K_p and self.state == GAME_STATE_OPENING:
                self.display_list.pop()
                self.display_list.append(GameDisplay(self.screen))
                self.state = GAME_STATE_CRIBBAGE

    def _process_mouse_event(self, evt):
        for obj in self.display_list[::-1]:
            if obj.handle_mouse_event(evt):
                return
        # no default mouse handling required

    def run(self):
        clock = pygame.time.Clock()
        self.display_list.append(GameIntro(self.screen))
        while True:
            elapsed = clock.tick(40)
            self.update(elapsed)
            self.draw()
            self._check_input()
