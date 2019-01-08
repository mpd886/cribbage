import pygame


class GraphicsObject:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def clear_screen(self, color=(0, 0, 0)):
        """
        Fills the screen with the given color (default=black)
        :return:
        """
        self.screen.fill(color, self.screen.get_rect())

    def blit(self, source, position):
        self.screen.blit(source, position)

    def flip(self):
        pygame.display.flip()

    def get_rect(self):
        return self.screen.get_rect()
