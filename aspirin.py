from __future__ import print_function
import pygame, sys
from pygame.locals import *

#constants
screenwidth = 800
screenheight = 600

class Player:
	def __init__(self):
		self.x = 20
		self.y = 20
		self.alive = True
		self.collected = 0


class Ball:
	def __init__(self, x, y, direction, velocity):
		self.r = 5
		self.rectangle = Rect(x - r, y - r, r * 2, r * 2)
		self.direction = direction
		self.velocity = velocity

	def move(self):
		if direction == 'left':
			rectangle.x -= velocity
			if rectangle.left < 0:
				rectangle.x = r
				direction = right
		elif direction == 'right':
			rectangle.x += velocity
			if rectangle.right > screenwidth:
				rectangle.x = screenwidth - r
				direction = 'left'
		elif direction == 'up':
			rectangle.y -= velocity
			if rectangle.top < 0:
				rectangle.y = r
				direction = 'down'
		elif direction == 'down':
			rectangle.y += velocity
			if rectangle.bottom > screenheight:
				rectangle.y = screenheight - r
				direction = 'up'

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Aspirin, game by Mitsuru Otsuka')
