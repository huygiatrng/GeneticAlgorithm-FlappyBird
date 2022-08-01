from settings import *
import pygame as pg

class Ground(pg.sprite.Sprite):
	def __init__(self,x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = sand_img
		self.image = pg.transform.scale(self.image, (w, h))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
