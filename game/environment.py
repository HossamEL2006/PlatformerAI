class Environment:
    def __init__(self) -> None:
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def clear_environment(self):
        self.objects.clear()
