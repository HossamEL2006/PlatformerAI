import numpy as np
import pygame 
from math import sqrt

pygame.init()

class pique():
    # triangle equilatéral
    def __init__(self, surface, taille, pos):
        self.surface = surface
        base = (2 * height * sqrt(3)) / 3
        self.point = ()


    def draw(self):
        pygame.draw(self.surface, self.rect)

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((680, 480))
        self.clock = pygame.time.Clock()

        self.loop_ = True
    
    def loop(self):
        while self.loop_:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop_ = False

            self.window.fill(pygame.Color(20, 20, 20))

            pygame.display.flip()
            # self.clock.tick(30)
    
    def quit(self):
        pygame.quit()

game = Game()
game.loop()
game.quit()