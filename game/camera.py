
from pygame import Surface

class Camera:
    def __init__(self, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wh_ratio = w/h
        self.is_set_up = False
        self.tiles_per_camera_width = None
        self.tiles_per_camera_height = None
        self.tile_size = None
        self.background = None
        
    def setup_by_width(self, tiles_per_camera_width):
        self.tiles_per_camera_width = tiles_per_camera_width
        self.tile_size = self.w / tiles_per_camera_width
        self.tiles_per_camera_height = self.tiles_per_camera_width / self.wh_ratio
        self.is_set_up = True
    
    def setup_by_height(self, tiles_per_camera_height):
        self.tiles_per_camera_height = tiles_per_camera_height
        self.tile_size = self.h / tiles_per_camera_height
        self.tiles_per_camera_width = self.tiles_per_camera_height * self.wh_ratio
        self.is_set_up = True
        
    def render(self, environment):
        if not self.is_set_up:
            raise RuntimeError("You must set up the camera first before using it")
        surface = Surface((self.w, self.h))
        if self.background:
            surface.blit(self.background, (0, 0))
        for object in environment.objects:
            object.draw(surface, self)
        return surface
