from __future__ import print_function
import pygame, sys
from pygame.locals import *
from random import randint

#constants
screenwidth = 800
screenheight = 600

class Player:
	def __init__(self):
		self.x = 20
		self.y = 20
		self.pspeed = 4
		self.r = 5
		self.alive = True
		self.collected = 0

	def move(self, l, r, u, d):
		global screenwidth, screenheight
		if l:
			x -= pspeed
			if x < 0:
				x = r
		if r:
			x += pspeed
			if x > screenwidth:
				x = screenwidth - r
		if u:
			y -= pspeed
			if y < 0:
				y = r
		if d:
			y += pspeed
			if y > screenheight:
				y = screenheight - r
		def getpos(self):
			return (rectangle.left, rectangle.top)


class PointBall:
	def __init__(self, (x, y)):
		self.r = 3
		self.rectangle = Rect(x - r, y - r, r * 2, r * 2)

	def getpos(self):
		return (rectangle.left, rectangle.top)

class Ball:
	def __init__(self, (x, y), direction, velocity):
		self.r = 3
		self.rectangle = Rect(x - r, y - r, r * 2, r * 2)
		self.direction = direction
		self.velocity = velocity

	def move(self):
		global screenwidth, screenheight
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

	def getpos(self):
		return (rectangle.left, rectangle.top)


def randloc():
	global screenwidth, screenheight
	return (randint(5, screenwidth), randint(5, screenheight))


pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Aspirin, game by Mitsuru Otsuka')

fontObj = pygame.font.Font('freesansbold.ttf', 32)
gameover = 'Game Over'
yourscore = 'Your Score:'

balllist = []
pointball = PointBall(randloc())
player = Player()
isPlaying = True
left=right=up=down=False
while isPlaying:
	windowSurfaceObj.fill(whiteColor)
	for i, b in enumerate(balllist): #move balls then draw them
		balllist[i].move()
		pygame.draw.circle(windowSurfaceObj, pygame.Color(255, 0, 0), b.getpos(), b.r)
	pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 255, 0), pointball.getpos(), pointball.r)
	pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 0, 255), player.getpos(), player.r)
