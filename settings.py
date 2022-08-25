import pygame as pg

pg.mixer.init()

WIDTH, HEIGHT = 400, 600

# Colors
# Primary Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SAND = (255, 255, 100)
YELLOW = (255, 255, 0)
ORANGE = (255, 255, 127)

FPS = 100

GRAVITY = 0.5 * HEIGHT / 600
sand_img = pg.image.load("images/sand.png")
SAND_HEIGHT = int(HEIGHT / 12)

tube_img = pg.image.load("images/tube.png")
JUMP_VELOCITY = int(-10 * HEIGHT / 600)
TUBE_VELOCITY = int(-3 * WIDTH / 400)
TUBE_WIDTH = int(WIDTH / 4)
TUBE_HEIGHT = int(5 * HEIGHT / 4)
SKY_WIDTH = int(WIDTH / 4)
TUBE_GAP = int(HEIGHT / 4)

bird_img = pg.image.load("images/bird.png")
bird_img = pg.transform.scale(bird_img, (int(34 * WIDTH / 400), int(24 * HEIGHT / 600)))
BIRD_SIZE = bird_img.get_size()
FLAP_COOLDOWN = 20
TURN_COEFFICIENT = -5

POPULATION = 200

INPUT_LAYER = 5
HIDDEN_LAYER = 4
OUTPUT_LAYER = 1
TOTAL_WEIGHT = (INPUT_LAYER + 1) * HIDDEN_LAYER + (HIDDEN_LAYER + 1) * OUTPUT_LAYER

THRESHOLD = 0.5

FITNESS_RATE = 1

MUTATION_RATE = 0.7
CROSSOVER_RATE = 0.6
SELECTION_RATE = 0.1  # 0.15

SELECTION_PERCENTAGE = 0.1
MUTATION_PERCENTAGE = 0.60  # 0.55
CROSSOVER_PERCENTAGE = 0.1  # 0.15
# RANDOM_RATE = 0.20

Background = pg.image.load("images/background.png")
Background = pg.transform.scale(Background, (WIDTH, Background.get_height() * WIDTH / Background.get_width()))

MEMORY_SIZE = 100_000
GAMMA = 0.995
ALPHA = 1e-3
NUM_STEPS_FOR_UPDATE = 4
