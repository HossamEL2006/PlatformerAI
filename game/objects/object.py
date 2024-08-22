
class Object:
    """ This class servs as a base layer of any object off the game
        All objects should inherit from this base class """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def draw(self, surface, camera):
        pass
