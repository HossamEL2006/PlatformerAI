from PIL import Image  # pip install pillow
import numpy as np
import pygame
import os
from numpy_to_pygame import ndarray_to_surface


def png_to_ndarray(png_path):
    img = Image.open(png_path)
    img_array = np.array(img)
    # On a 800x600 image, PIL returns a 600x800x3 array
    # We need it to be an 800x600x3 array though
    # So we should sway the X axis and Y axis by doing this:
    img_array = np.transpose(img_array, (1, 0, 2))  # (0, 1, 2) -> (1, 0, 2) (swap X and Y)
    return img_array


IMAGE_PATH = os.path.join(os.path.dirname(__file__), '../assets/test/800x600_test.png')
IMAGE_ARRAY = png_to_ndarray(IMAGE_PATH)
WINDOW = pygame.display.set_mode((800, 600))


def main():
    print(IMAGE_ARRAY)
    print(IMAGE_ARRAY.shape)  # (600, 800, 3)

    loop = True

    while loop:
        # EVENT DETECTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # DISPLAY
        WINDOW.blit(ndarray_to_surface(IMAGE_ARRAY), (0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
