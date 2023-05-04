from settings import *
from Bird import *
from Tube import *

class Sensor:
    def __init__(self):
        self.dist_vertical = 0 #distance from bird to middle point of the distance between 2 tubes
        self.dist_horizontal = 0 #distance from bird to tube

    def detect(self, bird, tube_top, tube_bottom):
        self.dist_horizontal = tube_bottom.rect.x + TUBE_WIDTH - bird.rect.center[0]
        true_tube_top_height = tube_top.height + tube_top.rect.y
        self.dist_vertical = ((tube_bottom.rect.y - true_tube_top_height)/2 + true_tube_top_height) - bird.rect.center[1]

    def detectAndReturn(self, bird, tube_top, tube_bottom):
        self.dist_horizontal = tube_bottom.rect.x + TUBE_WIDTH - bird.rect.center[0]
        true_tube_top_height = tube_top.height + tube_top.rect.y
        self.dist_vertical = ((tube_bottom.rect.y - true_tube_top_height) / 2 + true_tube_top_height) - bird.rect.center[1]
        return (self.dist_horizontal,true_tube_top_height,self.dist_vertical)
    # def draw(self):
    #     pass