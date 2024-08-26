import os
import pygame
from objects.object import Object


class Platform(Object):
    h = 1
    LEFT_SPRITE = None
    MIDDLE_SPRITE = None
    RIGHT_SPRITE = None
    TILE_SIZE = None

    _sprite_cache = {}  # Cache to store generated sprites
    # This optimises the game by storing previosly rendered platforms (with the same lenght)

    @classmethod
    def load_sprites(cls):
        """
        Load the platform sprites if they haven't been loaded yet.
        This function was built to avoid loading a png image before creating the game window which
        raises the following error:
          pygame.error: No video mode has been set
        This function is only called after pygame.displat.set_mode which solves the problem
        """
        if cls.LEFT_SPRITE is None:
            cls.LEFT_SPRITE = pygame.image.load(
                os.path.join(os.path.dirname(__file__),
                             "../../assets/kenney_platformer-art-pixel-redux/Tiles/tile_0125.png")
            ).convert_alpha()
        if cls.MIDDLE_SPRITE is None:
            cls.MIDDLE_SPRITE = pygame.image.load(
                os.path.join(os.path.dirname(__file__),
                             "../../assets/kenney_platformer-art-pixel-redux/Tiles/tile_0123.png")
            ).convert_alpha()
        if cls.RIGHT_SPRITE is None:
            cls.RIGHT_SPRITE = pygame.image.load(
                os.path.join(os.path.dirname(__file__),
                             "../../assets/kenney_platformer-art-pixel-redux/Tiles/tile_0155.png")
            ).convert_alpha()

        if cls.TILE_SIZE is None:
            cls.TILE_SIZE = cls.LEFT_SPRITE.get_width()

    def __init__(self, x, y, length) -> None:
        """Initialize the platform."""
        # Load the sprites when the first platform is created
        Platform.load_sprites()

        super().__init__(x, y, length, Platform.h, self.generate_platform_sprite(length))

    @staticmethod
    def generate_platform_sprite(length):
        """Generate a surface for the platform based on the length, using caching."""
        if length in Platform._sprite_cache:
            return Platform._sprite_cache[length]

        surface = pygame.Surface((Platform.TILE_SIZE * length, Platform.TILE_SIZE), pygame.SRCALPHA)
        surface.blit(Platform.LEFT_SPRITE, (0, 0))
        for i in range(1, length - 1):
            surface.blit(Platform.MIDDLE_SPRITE, (i * Platform.TILE_SIZE, 0))
        surface.blit(Platform.RIGHT_SPRITE, ((length - 1) * Platform.TILE_SIZE, 0))

        # Store the generated surface in the cache
        Platform._sprite_cache[length] = surface

        return surface
