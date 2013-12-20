from __future__ import print_function
import pygame, sys
from pygame.locals import *
from random import randint
from time import sleep

#constants
screenwidth = 800
screenheight = 600

class Player:
	def __init__(self):
		self.x = 20
		self.y = 20
		self.pspeed = 6
		self.r = 10
		self.alive = True
		self.collected = 0

	#x, y should be center
	def move(self, l, r, u, d):
		global screenwidth, screenheight
		#print(str(self.x) + " " + str(self.y))
		if l:
			self.x -= self.pspeed
			if self.x - self.r < 0:
				self.x = self.r
		if r:	
			self.x += self.pspeed
			if self.x + self.r > screenwidth:
				self.x = screenwidth - self.r
		if u:
			self.y -= self.pspeed
			if self.y - self.r < 0:
				self.y = self.r
		if d:
			self.y += self.pspeed
			if self.y + self.r > screenheight:
				self.y = screenheight - self.r

	def getcenter(self):
		return (self.x, self.y)

	def getpos(self):
		return (self.x - self.r, self.y - self.r)


class PointBall:
	def __init__(self, loc):
		self.r = 8
		self.x = loc[0]
		self.y = loc[1]

	def getcenter(self):
		return (self.x, self.y)

	def getpos(self):
		return (self.x - self.r, self.y - self.r)

class Ball:
	def __init__(self, direction):
		self.r = 8
		self.x = randint(10, screenwidth - 10)
		self.y = randint(10, screenheight - 10)
		self.direction = direction
		self.velocity = randint(3, 15)

	def move(self):
		global screenwidth, screenheight
		if self.direction == 'left':
			self.x -= self.velocity
			if self.x - self.r < 0:
				self.x = self.r
				self.direction = 'right'
		elif self.direction == 'right':
			self.x += self.velocity
			if self.x + self.r > screenwidth:
				self.x = screenwidth - self.r
				self.direction = 'left'
		elif self.direction == 'up':
			self.y -= self.velocity
			if self.y - self.r < 0:
				self.y = self.r
				self.direction = 'down'
		elif self.direction == 'down':
			self.y += self.velocity
			if self.y + self.r > screenheight:
				self.y = screenheight - self.r
				self.direction = 'up'

	def getcenter(self):
		return (self.x, self.y)

	def getpos(self):
		return (self.x - self.r, self.y - self.r)


def randloc():
	global screenwidth, screenheight
	return (randint(10, screenwidth - 10), randint(10, screenheight - 10))


def collided(player, ball):
	playercenter = player.getcenter()
	ballcenter = ball.getcenter()
	dx = ballcenter[0] - playercenter[0]
	dy = ballcenter[1] - playercenter[1]
	radii = ball.r + player.r
	return dx * dx + dy * dy < radii * radii


pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Aspirin, game by Mitsuru Otsuka')

fontObj = pygame.font.Font('freesansbold.ttf', 14)
gameover = 'Game Over'
yourscore = 'Your Score:'
while True:
	balllist = []
	pointball = PointBall(randloc())
	player = Player()
	left=right=up=down=False
	while player.alive:
		windowSurfaceObj.fill(pygame.Color(255, 255, 255))
		#draw the point ball
		pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 255, 0), pointball.getcenter(), pointball.r)
		if collided(player, pointball):
			player.collected += 1
			pointball = PointBall(randloc())
			if randint(0, 1) == 0:
				balllist.append(Ball('left'))
			else:
				balllist.append(Ball('right'))
			if randint(0, 1) == 0:
				balllist.append(Ball('up'))
			else:
				balllist.append(Ball('down'))
		#move and draw player
		player.move(left, right, up, down)
		pygame.draw.circle(windowSurfaceObj, pygame.Color(0, 0, 255), player.getcenter(), player.r)
		for i, b in enumerate(balllist): #move balls then draw them
			balllist[i].move()
			pygame.draw.circle(windowSurfaceObj, pygame.Color(255, 0, 0), b.getcenter(), b.r)
			if collided(player, b):
				player.alive = False
		msgSurfaceObj = fontObj.render(str(yourscore) + str(player.collected), False, pygame.Color(0, 0, 0))
		msgRectobj = msgSurfaceObj.get_rect()
		msgRectobj.bottomleft = (5, screenheight - 5)
		windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
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

	msgSurfaceObj = fontObj.render(str(yourscore) + str(player.collected), False, pygame.Color(0, 0, 0))
	msgRectobj = msgSurfaceObj.get_rect()
	msgRectobj.bottomleft = (5, screenheight - 5)
	windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

	msgSurfaceObj = fontObj.render(str(gameover), False, pygame.Color(0, 0, 0))
	msgRectobj = msgSurfaceObj.get_rect()
	msgRectobj.bottomleft = (screenwidth / 2 - msgRectobj.width / 2, screenheight / 2 - msgRectobj.height / 2)
	windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)
	pygame.display.update()
	sleep(3)