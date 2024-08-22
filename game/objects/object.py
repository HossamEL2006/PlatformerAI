class Object:
    """
    This class serves as the base class for any object in the game.
    All game objects (such as bricks, players, enemies, etc.) should inherit from this base class.
    """

    def __init__(self, x, y) -> None:
        """
        Initialize a generic game object at a specific location in the game world.

        Parameters:
        x (float): The x-coordinate of the object's position in the game world.
        y (float): The y-coordinate of the object's position in the game world.
        """
        self.x = x
        self.y = y

    def draw(self, surface, camera):
        """
        Draw the object on the given surface using the camera's perspective.
        This method is intended to be overridden by subclasses.

        Parameters:
        surface (Surface): The Pygame surface on which to draw the object.
        camera (Camera): The Camera object that provides the perspective for drawing.
        """
        # This method should be implemented by subclasses
