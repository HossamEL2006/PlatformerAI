from pygame import Surface


class Camera:
    def __init__(self, x, y, w, h) -> None:
        """
        Initialize the Camera object with position, dimensions, and other properties.

        Parameters:
        x (float): The x-coordinate of the camera's position.
        y (float): The y-coordinate of the camera's position.
        w (int): The width of the camera view in pixels.
        h (int): The height of the camera view in pixels.
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wh_ratio = w / h  # Calculate the width-to-height ratio
        self.is_set_up = False  # Flag to ensure the camera is set up before rendering
        self.tiles_per_camera_width = None  # Number of tiles fitting the camera's width
        self.tiles_per_camera_height = None  # Number of tiles fitting the camera's height
        self.tile_size = None  # Size of a single tile in pixels
        self.background = None  # Background image to be used during rendering

    def setup_by_width(self, tiles_per_camera_width):
        """
        Set up the camera based on the desired number of tiles that fit within the camera's width.

        Parameters:
        tiles_per_camera_width (int): The number of tiles that fit horizontally in the
                                      camera's view.
        """
        self.tiles_per_camera_width = tiles_per_camera_width
        self.tile_size = self.w / tiles_per_camera_width  # Calculate the size of each tile
        self.tiles_per_camera_height = self.tiles_per_camera_width / \
            self.wh_ratio  # Calculate the corresponding number of vertical tiles
        self.is_set_up = True  # Mark the camera as set up

    def setup_by_height(self, tiles_per_camera_height):
        """
        Set up the camera based on the desired number of tiles that fit within the camera's height.

        Parameters:
        tiles_per_camera_height (int): The number of tiles that fit vertically in the camera's view.
        """
        self.tiles_per_camera_height = tiles_per_camera_height
        self.tile_size = self.h / tiles_per_camera_height  # Calculate the size of each tile
        self.tiles_per_camera_width = self.tiles_per_camera_height * \
            self.wh_ratio  # Calculate the corresponding number of horizontal tiles
        self.is_set_up = True  # Mark the camera as set up

    def render(self, environment):
        """
        Render the current view of the environment from the camera's perspective.

        Parameters:
        environment (Environment): The game environment containing objects to be rendered.

        Returns:
        Surface: A Pygame Surface object with the rendered view.
        """
        if not self.is_set_up:
            raise RuntimeError("You must set up the camera first before using it")

        surface = Surface((self.w, self.h))  # Create a new surface for the camera's view

        if self.background:
            surface.blit(self.background, (0, 0))  # Draw the background image onto the surface

        # Draw each object in the environment onto the surface, using the camera's perspective
        for obj in environment.objects:
            obj.draw(surface, self)

        return surface  # Return the rendered surface
