class Environment:
    def __init__(self) -> None:
        """
        Initialize the Environment object, which manages all game objects within the game world.
        """
        self.objects = []  # List to hold all game objects in the environment

    def add_object(self, obj):
        """
        Add a game object to the environment.
        
        Parameters:
        obj (object): The game object to be added to the environment. This could be anything that
                      interacts within the game world, such as a brick, player, or enemy.
        """
        self.objects.append(obj)  # Add the object to the environment's list of objects

    def clear_environment(self):
        """
        Remove all objects from the environment, effectively clearing the game world.
        """
        self.objects.clear()  # Clear the list of objects, removing all items from the environment
