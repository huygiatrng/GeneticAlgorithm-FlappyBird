from settings import *

vec2 = pg.math.Vector2


class Tube(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, direction):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface((w,h))
        self.image = tube_img
        self.image = pg.transform.scale(self.image, (w, h))
        if direction == 0:
            self.image = pg.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.height = h

        # This is the tubes x velocity, giving the appearance of the player moving
        self.velX = TUBE_VELOCITY

    def update(self):
        self.rect.x += self.velX
        # If a tube goes of the screen then it is 'killed'
        if self.rect.x + WIDTH / 4 < 0:
            self.kill()
