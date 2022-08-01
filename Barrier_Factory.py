from Sky import *
from Bird import *
from Ground import *
from settings import *
import random

#Design Pattern : Factory
class Barrier_Factory:
    def __init__(self):
        self.index = 0
        self.__list_tube_height = []

        for i in range(1,3000):
            self.__list_tube_height.append(random.randint(10,HEIGHT - SAND_HEIGHT - TUBE_GAP- 10))

        self.count = 0

        tube = Tube(0,0,0,0,0)
        sky = Sky(0,0,0,0)
        ground = Ground(0,0,0,0)

        self.dict = {"Tube": type(tube), "Sky" : type(sky), "Ground": type(ground)}

    def generate(self, barrier_name):


        if barrier_name == "Sky":
            sky = Sky(0,-100,WIDTH,SKY_WIDTH)
            if type(sky) is self.dict["Sky"]:
                return sky

        if barrier_name == "Tube":
            TUBE_Y = random.randint(20,HEIGHT - SAND_HEIGHT - TUBE_GAP - 20)-TUBE_HEIGHT
            #TUBE_HEIGHT = self.__list_tube_height[self.index]
            self.index += 1
            tubeTop = Tube(WIDTH, TUBE_Y, TUBE_WIDTH, TUBE_HEIGHT, 1)
            tubeBottom = Tube(WIDTH, TUBE_Y + TUBE_HEIGHT + TUBE_GAP, TUBE_WIDTH,TUBE_HEIGHT , 0)
            # HEIGHT - SAND_HEIGHT - (TUBE_HEIGHT + TUBE_GAP)
            self.count += 1
            if type(tubeTop) and type(tubeBottom) is self.dict["Tube"]:
                return tubeTop, tubeBottom

        if barrier_name == "Ground":
            ground = Ground(0,HEIGHT-SAND_HEIGHT,WIDTH,SAND_HEIGHT)
            if type(ground) is self.dict["Ground"]:
                return ground

        raise NameError("Wrong factory format")