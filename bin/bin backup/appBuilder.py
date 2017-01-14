#!/usr/bin/env python

remixer_image_filename = '../Media/mixer1.jpg'
rpi_image_filename = '../Media/pi.jpg'
new_image_filename = '../Media/new.jpg'
talkBox_image_filename = '../Media/talkBox.jpg'
remixerSmall_image_filename = '../Media/mixer2.jpg'
rpiSmall_image_filename = '../Media/pi.png'



import pygame
import os
from sys import exit
from pygame.locals import *
from pygame import Rect

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

screen = pygame.display.set_mode((480, 320), 0, 32)
screen.fill((255, 255, 255))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
pygame.display.set_caption("reMixer")

remixer = pygame.image.load(remixer_image_filename).convert()
rpi = pygame.image.load(rpi_image_filename).convert()
remixerSmall = pygame.image.load(remixerSmall_image_filename).convert()
rpiSmall = pygame.image.load(rpiSmall_image_filename).convert()


remixer_rect = pygame.Rect(5,20,250,240)
rpi_rect = pygame.Rect(220,28,250,221)
remixerSmall_rect = pygame.Rect(5,20,250,240)
rpiSmall_rect = pygame.Rect(220,28,250,221)


pageNumber = 1

#pygame.mouse.set_visible(False)

while True:

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
		if pageNumber == 1:

			if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP: 
				x, y = event.pos
				if pygame.Rect(rpi_rect).collidepoint(x,y): 
					pygame.quit()
					exit()
				if pygame.Rect(remixer_rect).collidepoint(x,y):
					pageNumber = 2

			remixer_rect = (5,20,250,240)
			rpi_rect = (220,28,250,221)
        		background.blit(remixer, (5,20))
			background.blit(rpi, (220,28))
			screen.blit(background, (0,0))
			pygame.display.update()
		elif pageNumber == 2:
			remixerSmall_rect = (5,20,250,240)
                        rpiSmall_rect = (220,28,250,221)
			screen.fill((255, 255, 255))
			background.fill((255, 255, 255))
			background.blit(remixerSmall, (5,20))
                        background.blit(rpiSmall, (220,28))
			screen.blit(background, (0,0))
                        pygame.display.update()

			if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                               x, y = event.pos
                               if pygame.Rect(rpi_rect).collidepoint(x,y):
                                       pygame.quit()
                                       exit()
                               if pygame.Rect(remixer_rect).collidepoint(x,y):
                                       print 'here'
			
