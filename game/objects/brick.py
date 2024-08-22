
import pygame
from .object import Object
import os


PATH = os.path.join(os.path.dirname(__file__), '../../assets/test/brick.png')
SPRITE = pygame.image.load(PATH)


class Brick(Object):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.w = 1
        self.h = 1

    def draw(self, surface, camera):
        tile_size = camera.tile_size
        scaled_image = pygame.transform.scale(SPRITE, (int(tile_size), int(tile_size)))
        surface.blit(scaled_image, (tile_size*(self.x-camera.x), tile_size*(self.y-camera.y)))
