class Object:
    """
    This class serves as the base class for any object in the game.
    All game objects (such as bricks, players, enemies, etc.) should inherit from this base class.
    """

    def __init__(self, x, y, w, h, sprite) -> None:
        """
        Initialize a generic game object at a specific location in the game world.

        Parameters:
        x (float): The x-coordinate of the object's position in the game world.
        y (float): The y-coordinate of the object's position in the game world.
        w (float): The
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sprite = sprite
        self.is_visible = True
