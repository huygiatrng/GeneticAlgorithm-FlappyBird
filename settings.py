import pygame as pg
pg.mixer.init()

WIDTH, HEIGHT = 400,600

# Colors
# Primary Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
SAND = (255,255,100)
YELLOW = (255,255,0)
ORANGE = (255,255,127)

FPS = 100

GRAVITY = 0.5
sand_img = pg.image.load("images/sand.png")
SAND_HEIGHT = 50

tube_img = pg.image.load("images/tube.png")
JUMP_VELOCITY = -10
TUBE_VELOCITY = -3
TUBE_WIDTH = 100
TUBE_HEIGHT = 480
SKY_WIDTH = 100
TUBE_GAP = 150

bird_img = pg.image.load("images/bird.png")
BIRD_SIZE = bird_img.get_size()
FLAP_COOLDOWN = 20
TURN_COEFFICIENT = -5

POPULATION = 150

INPUT_LAYER = 5
HIDDEN_LAYER = 4
OUTPUT_LAYER = 1
TOTAL_WEIGHT = (INPUT_LAYER+1)*HIDDEN_LAYER + (HIDDEN_LAYER+1)*OUTPUT_LAYER

THRESHOLD = 0.5

FITNESS_RATE = 1

MUTATION_RATE = 0.7
CROSSOVER_RATE = 0.6
SELECTION_RATE = 0.1 #0.15

SELECTION_PERCENTAGE = 0.1
MUTATION_PERCENTAGE = 0.60 #0.55
CROSSOVER_PERCENTAGE = 0.1 #0.15
#RANDOM_RATE = 0.20

Background = pg.image.load("images/background.png")


MEMORY_SIZE = 100_000
GAMMA = 0.995
ALPHA = 1e-3
NUM_STEPS_FOR_UPDATE = 4