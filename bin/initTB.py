#This code was created by Foad Hamidi and modified by David Yin
#Version 1: November 2016

#This code initializes all global variables used by the talkbox program

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import os
import time
from sys import exit
from pygame.locals import *
from pygame import Rect

#These are needed to use touchscreen
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

#Initialize pygame
pygame.init()

#Initializing the screen using dimensions of 3.5inch TFT Resistive Touchscreen
screen = pygame.display.set_mode((480, 320), 0, 32) #pygame.FULLSCREEN, 32)
screen.fill((255, 255, 255))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
pygame.display.set_caption("reMixer")

#Loading all the needed image files
remixer = pygame.image.load('../Media/remixer.jpg').convert()
rpi = pygame.image.load('../Media/rpi.png').convert_alpha()
remixerTiny = pygame.image.load('../Media/remixerTiny.jpg').convert()
rpiTiny = pygame.image.load('../Media/rpiTiny.jpg').convert()
talkBox = pygame.image.load('../Media/talkbox.jpg').convert()
newIcon = pygame.image.load('../Media/newIcon.png').convert_alpha()
talkBoxTiny = pygame.image.load('../Media/talkBoxTiny.jpg').convert()
inputIcon = pygame.image.load('../Media/inputIcon.jpg').convert_alpha()
processIcon = pygame.image.load('../Media/processIconOn.jpg').convert_alpha()
outputIcon = pygame.image.load('../Media/outputIcon.jpg').convert_alpha()
newIconTiny = pygame.image.load('../Media/newIconTiny.png').convert_alpha()
processIconOn = pygame.image.load('../Media/processIcon.jpg').convert_alpha()
outputIconOn = pygame.image.load('../Media/outputIconOn.jpg').convert_alpha()
inputIconOn = pygame.image.load('../Media/inputIconOn.jpg').convert_alpha()

#Creating rectangles for all the images to detect touch input
remixer_rect = pygame.Rect(5,20,250,240)
rpi_rect = pygame.Rect(220,28,250,221)
remixerTiny_rect = pygame.Rect(20, 0, 100, 113)
rpiTiny_rect = pygame.Rect(350, 0, 100, 88)
talkBox_rect = pygame.Rect(280, 110, 200, 200)
newIcon_rect = pygame.Rect(10, 130, 210, 168)
