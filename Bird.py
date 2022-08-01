from Sensor import *
from NeuronNetwork import *
from Sensor import *

vec2 = pg.math.Vector2


class Bird(pg.sprite.Sprite):
    def __init__(self, genome=None):
        pg.sprite.Sprite.__init__(self)
        self.ori_img = bird_img
        self.image = self.ori_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, random.randint(15, HEIGHT - SAND_HEIGHT) - 5)
        self.angle_direction = 0

        # self.pos = vec2(WIDTH/2, HEIGHT/2)
        self.pos = vec2(WIDTH / 2, random.randint(15, HEIGHT - SAND_HEIGHT) - 5)
        self.vel = vec2(0, 0)
        self.acc = vec2(0, GRAVITY)
        self.live = 1
        self.sensor = Sensor()
        self.count = 0
        if genome is None:
            self.NeurolNetwork = NeurolNetwork()
        else:
            self.NeurolNetwork = NeurolNetwork(genome)

    def update(self):
        self.count+=1
        if self.vel[1] > 8:
            self.vel[1] = 8
        else:
            self.vel += self.acc
            self.pos += self.vel + self.acc
        if self.live == 1:  # if bird alive then increase fitness
            self.image = pg.transform.rotate(self.ori_img, self.vel.y * (TURN_COEFFICIENT))
            self.rect.center = (
            self.pos[0] - int(self.image.get_width() / 2), self.pos[1] - int(self.image.get_height() / 2))
            self.NeurolNetwork.fitness += FITNESS_RATE

    def flap(self):
        if self.count>FLAP_COOLDOWN:
            self.vel.y = JUMP_VELOCITY
            self.count=0
        # self.image = pg.transform.rotate(self.ori_img, -30)
