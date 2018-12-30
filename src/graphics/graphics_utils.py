import pygame
import os


IMAGES_BASE_DIRECTORY = r'D:\Development\Cribbage\images'
CARD_BACK_IMAGE = "back.png"
COLOR_BLACK = (0, 0, 0)
COLOR_DARK_GREEN = (7, 68, 2)


def load_card_images(directory, scale=None):
    """
    Finds all card images (for now, any image that isn't called 'back.png'
    :param directory:
    :param scale: if not None, should be new size to scale images to
    :return: list of pygame Surfaces
    """
    images = []
    for f in os.listdir(directory):
        if f.lower() != CARD_BACK_IMAGE:
            img = pygame.image.load(os.path.join(directory, f))
            if scale is not None:
                img = pygame.transform.scale(img, scale)
            images.append(img)
    return images
