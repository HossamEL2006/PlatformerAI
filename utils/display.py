from PIL import Image  # pip install pillow
import numpy as np
import pygame


def png_to_ndarray(png_path: str):
    """ This function takes the path to a png image as input and returns an ndarray
        (width x height x 3) containing each pixel's color in RGB """
    img = Image.open(png_path)
    img_array = np.array(img)
    # On a 800x600 image, PIL returns a 600x800x3 array
    # We need it to be an 800x600x3 array though
    # So we should sway the X axis and Y axis by doing this:
    img_array = np.transpose(img_array, (1, 0, 2))  # (0, 1, 2) -> (1, 0, 2) (swap X and Y)
    return img_array


def ndarray_to_surface(array: np.ndarray):
    """ This function takes as imput a (Width x Height x 3) numpy ndarray and transforms it
        into a pygame.Surface """
    return pygame.surfarray.make_surface(array)


def inspect_pygame_surface(surface: pygame.Surface):
    """ This function takes as input a pygame.Surface and draws it on a pygame screen with the
        same dimensions (mainly for debugging purposes) """
    w, h = surface.get_width(), surface.get_height()
    window = pygame.display.set_mode((w, h))
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        window.blit(surface, (0, 0))
        pygame.display.flip()


# TEST
if __name__ == '__main__':
    PATH = 'assets/test/800x600_test.png'
    inspect_pygame_surface(
        ndarray_to_surface(
            png_to_ndarray(
                PATH
            )
        )
    )
