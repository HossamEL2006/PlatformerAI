
import pygame
import os
from camera import Camera
from environment import Environment
from objects.brick import Brick


W, H = 640, 480
BG = pygame.image.load(
    os.path.join(os.path.dirname(__file__), '../assets/bg.jpg')
)


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((W, H))
        self.camera = Camera(-3, -5, W, H)
        self.camera.setup_by_width(20)
        self.camera.background = BG
        self.environment = Environment()
        self.clock = pygame.time.Clock()
        self.running = True

    def load_test_level(self):
        self.environment.add_object(Brick(-1, 5))
        self.environment.add_object(Brick(0, 5))
        self.environment.add_object(Brick(1, 5))
        self.environment.add_object(Brick(2, 5))
        self.environment.add_object(Brick(3, 5))
        
        self.environment.add_object(Brick(6, 3))
        self.environment.add_object(Brick(7, 3))
        self.environment.add_object(Brick(8, 3))
        self.environment.add_object(Brick(9, 3))
        
        self.environment.add_object(Brick(12, 4))
        self.environment.add_object(Brick(15, 4))

    def loop(self):
        while self.running:
            # EVENT DETECTION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # GAME LOGIC
            self.load_test_level()
            
            # DISPLAY
            surface = self.camera.render(self.environment)
            self.window.blit(surface, (0, 0))
            pygame.display.flip()
            
            # FPS
            self.clock.tick(60)

    def quit(self):
        pygame.quit()


game = Game()
game.loop()
game.quit()
