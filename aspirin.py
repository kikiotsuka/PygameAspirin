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

	#x, y should be center
	def move(self, l, r, u, d):
		global screenwidth, screenheight
		if l:
			self.x -= self.pspeed
			if self.x < 0:
				self.x = self.r
		if r:
			self.x += self.pspeed
			if self.x > screenwidth:
				self.x = screenwidth - self.r
		if u:
			self.y -= self.pspeed
			if self.y < 0:
				self.y = self.r
		if d:
			self.y += self.pspeed
			if self.y > screenheight:
				self.y = screenheight - self.r

	def getpos(self):
		return (self.x - self.r, self.y - self.r)


class PointBall:
	def __init__(self, x, y):
		self.r = 3
		self.x = x
		self.y = y

	def getpos(self):
		return (self.x - self.r, self.y - self.r)

class Ball:
	def __init__(self, x, y, direction, velocity):
		self.r = 4
		self.rectangle = Rect(x - r, y - r, r * 2, r * 2)
		self.direction = direction
		self.velocity = velocity

	def move(self):
		global screenwidth, screenheight
		if self.direction == 'left':
			self.rectangle.x -= self.velocity
			if self.rectangle.left < 0:
				self.rectangle.x = self.r
				self.direction = 'right'
		elif self.direction == 'right':
			self.rectangle.x += self.velocity
			if self.rectangle.right > screenwidth:
				self.rectangle.x = screenwidth - self.r
				self.direction = 'left'
		elif self.direction == 'up':
			self.rectangle.y -= self.velocity
			if self.rectangle.top < 0:
				self.rectangle.y = self.r
				self.direction = 'down'
		elif self.direction == 'down':
			self.rectangle.y += self.velocity
			if self.rectangle.bottom > screenheight:
				self.rectangle.y = screenheight - self.r
				self.direction = 'up'

	def getpos(self):
		return (self.rectangle.left, self.rectangle.top)


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
tmp = randloc()
pointball = PointBall(tmp[0], tmp[1])
player = Player()
left=right=up=down=False
while player.alive:
	windowSurfaceObj.fill(pygame.Color(255, 255, 255))
	#draw the point ball
	pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 255, 0), pointball.getpos(), pointball.r * 2)
	if (player.x - pointball.x) ** 2 + (player.y - pointball.y) ** 2 < (player.r + pointball.r) ** 2:
		player.collected += 1
		tmp = randloc()
		pointball = PointBall(tmp[0], tmp[1])
	#move and draw player
	player.move(left, right, up, down)
	pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 0, 255), player.getpos(), player.r * 2)
	for i, b in enumerate(balllist): #move balls then draw them
		balllist[i].move()
		pygame.draw.circle(windowSurfaceObj, pygame.Color(255, 0, 0), b.getpos(), b.r * 2)
		if (player.x - b.x) ** 2 + (player.y - b.y) ** 2 < (player.r + b.r) ** 2:
			player.alive = false
	#key listener
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key in (K_LEFT, K_a):
				left = True
			elif event.key in (K_RIGHT, K_d):
				right = True
			elif event.key in (K_DOWN, K_s):
				down = True
			elif event.key in (K_UP, K_w):
				up = True
			elif event.key == K_q:
				pygame.quit()
				sys.exit()
		elif event.type == KEYUP:
			if event.key in (K_LEFT, K_a):
				left = False
			elif event.key in (K_RIGHT, K_d):
				right = False
			elif event.key in (K_DOWN, K_s):
				down = False
			elif event.key in (K_UP, K_w):
				up = False

	pygame.display.update()
	fpsClock.tick(30)