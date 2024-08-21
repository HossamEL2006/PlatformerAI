import pygame
import numpy as np

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Numpy Array to Image")


class Player:
    def __init__(self) -> None:
        pass


def ndarray_to_surface(array):
    """ This function takes as imput a (Width x Height x 3) numpy ndarray and transforms it
        into a pygame.Surface """
    return pygame.surfarray.make_surface(array)


def main():
    # Create a NumPy array with the dimension (WIDTH x HEIGHT x 3) with  random values
    # The X and Y axis represent the different pixels
    # The Z axis represents the RGB values of the color of that specific pixel
    pixel_array = np.random.randint(0, 256, (WIDTH, HEIGHT, 3), dtype=np.uint8)

    loop = True

    while loop:
        # EVENT DETECTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # DISPLAY
        WINDOW.blit(ndarray_to_surface(pixel_array), (0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
