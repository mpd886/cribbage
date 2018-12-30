import sys
from utils import Point
import math
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

    def _opening(self):
        image = load_card_images(IMAGES_BASE_DIRECTORY, (100, 150))[0]
        card_back = pygame.image.load(os.path.join(IMAGES_BASE_DIRECTORY, CARD_BACK_IMAGE))
        circle_size = 0.5
        circle_speed = 0.2
        circle_grow_speed = 0.1
        center = self.center()
        x = center.x
        y = 0
        clock = pygame.time.Clock()
        theta = 0 # degrees
        while not self.stop_animation:
            self._check_input()
            # draw
            self.screen.fill(COLOR_BLACK, self.screen.get_rect())
            self.screen.blit(image, (x, center.y+y))
            pygame.display.flip()
            dt = clock.tick(40)
            theta = (theta + dt*circle_speed) % 360
            radians = math.radians(theta)
            x += math.sin(radians) * circle_size
            y += math.cos(radians) * circle_size
            circle_size += circle_grow_speed
            if circle_size >= 50 or circle_size <= 0:
                circle_grow_speed = -circle_grow_speed

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
