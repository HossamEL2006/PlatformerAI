import os
import pygame
from .object import Object


# Path to the brick sprite image
PATH = os.path.join(os.path.dirname(__file__), '../../assets/test/brick.png')
# Load the brick sprite
SPRITE = pygame.image.load(PATH)


class Brick(Object):
    def __init__(self, x, y) -> None:
        """
        Initialize a Brick object at a specific location in the game world.

        Parameters:
        x (float): The x-coordinate of the brick's position in the game world.
        y (float): The y-coordinate of the brick's position in the game world.
        """
        super().__init__(x, y)  # Call the parent class's initializer
        self.w = 1  # Set the width of the brick to 1 tile unit
        self.h = 1  # Set the height of the brick to 1 tile unit

    def draw(self, surface, camera):
        """
        Draw the brick on the given surface using the camera's perspective.

        Parameters:
        surface (Surface): The Pygame surface on which to draw the brick.
        camera (Camera): The Camera object that provides the perspective for drawing.
        """
        tile_size = camera.tile_size  # Get the size of a tile from the camera
        # Scale the brick sprite to match the tile size
        scaled_image = pygame.transform.scale(SPRITE, (int(tile_size), int(tile_size)))
        # Draw the scaled brick sprite on the surface at the correct position
        surface.blit(scaled_image, (tile_size * (self.x - camera.x),
                     tile_size * (self.y - camera.y)))
