import os
import pygame
from objects.object import Object


# Path to the brick sprite image
SPRITE_PATH = os.path.join(os.path.dirname(__file__), '../../assets/test/brick.png')


class Brick(Object):
    sprite = pygame.image.load(SPRITE_PATH)  # A brick has always the same sprite
    w, h = 1, 1  # Bricks always occupy one tile only

    def __init__(self, x, y) -> None:
        """
        Initialize a Brick object at a specific location in the game world.

        Parameters:
        x (float): The x-coordinate of the brick's position in the game world.
        y (float): The y-coordinate of the brick's position in the game world.
        """
        super().__init__(x, y, Brick.w, Brick.h, Brick.sprite)
