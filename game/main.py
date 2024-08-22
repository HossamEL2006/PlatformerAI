import os
import pygame
from camera import Camera
from environment import Environment
from objects.brick import Brick

# Constants for the window dimensions
W, H = 640, 480

# Load background image for the game, using the relative path to assets folder
BG = pygame.image.load(
    os.path.join(os.path.dirname(__file__), '../assets/bg.jpg')
)


class Game:
    def __init__(self):
        """
        Initialize the game environment, including setting up the window, camera, environment,
        clock, and the running state of the game.
        """
        pygame.init()
        self.window = pygame.display.set_mode((W, H))  # Initialize the game window
        self.camera = Camera(-3, -5, W, H)  # Initialize the camera with position and window size
        self.camera.setup_by_width(20)  # Setup the camera zoom or scale based on width
        self.camera.background = BG  # Set the background image for the camera
        self.environment = Environment()  # Initialize the environment to hold game objects
        self.clock = pygame.time.Clock()  # Setup the clock to control the game frame rate
        self.running = True  # Flag to indicate whether the game loop should keep running

        self.load_test_level()  # Load the test level every frame (This is problematic)

    def load_test_level(self):
        """
        Load a simple test level by adding brick objects to the environment.
        This method is called to create a basic level layout with bricks.
        """
        # Add bricks to the environment at specific positions
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
        """
        Main game loop. Handles events, game logic, rendering, and frame rate control.
        """
        while self.running:
            # EVENT DETECTION
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Exit the game loop if the quit event is triggered

            # DISPLAY
            # Render the environment through the camera
            surface = self.camera.render(self.environment)
            self.window.blit(surface, (0, 0))  # Draw the rendered surface onto the window
            pygame.display.flip()  # Update the display with the new frame

            # FPS
            self.clock.tick(60)  # Cap the frame rate to 60 FPS

    def quit(self):
        """
        Quit the game and clean up resources.
        """
        pygame.quit()  # Uninitialize all pygame modules


# Create a Game instance and start the game loop
game = Game()
game.loop()
game.quit()
