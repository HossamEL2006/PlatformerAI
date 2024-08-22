from math import sqrt
from object import Object
import pygame


class Spike(Object):
    # triangle equilatéral
    def __init__(self, surface, height, pos):
        super().__init__()
        self.surface = surface
        base = (2 * height * sqrt(3)) / 3
        self.point = ()

    def draw(self):
        pygame.blit(self.surface, self.rect)
