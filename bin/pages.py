#This code was created by Foad Hamidi and modified by David Yin
#Version 1: November 2016

#This code displays the various talkbox pages along with the icons and background

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import os
import time
from sys import exit
from pygame.locals import *
from pygame import Rect
from initTB import *

#Load icons and background for initial talbbox page
def loadIcons():
    #the colors of the icons are changed
	background.blit(inputIconOn, (10, 140))
	time.sleep(0.3)
	screen.blit(background, (0,0))
	pygame.display.update()
	background.blit(processIconOn, (145, 130))
	background.blit(inputIcon, (10, 140))
	time.sleep(0.3)
	screen.blit(background, (0,0))
	pygame.display.update()
	time.sleep(0.3)
	background.blit(processIcon, (145, 130))
	background.blit(outputIconOn, (305, 130))
	screen.blit(background, (0,0))
	pygame.display.update()
	time.sleep(0.3)
	background.blit(outputIcon, (305, 130))
	screen.blit(background, (0,0))
	pygame.display.update()

#Load icons and background for welcome page
def loadWelcomePage():
    	screen.fill((255, 255, 255))
    	background.fill((255, 255, 255))
    	background.blit(remixer, (5,20))
    	background.blit(rpi, (220,28))
    	screen.blit(background, (0,0))
    	pygame.display.update()

#Load icons and background for main page
def loadMainPage():
    	screen.fill((255, 255, 255))
	background.fill((255, 255, 255))
   	background.blit(remixerTiny, (20,0))
    	background.blit(newIcon, (10, 130))
   	background.blit(talkBox, (280, 110))
	background.blit(rpiTiny, (350,5))
	screen.blit(background, (0,0))
	pygame.display.update()

#Load icons and background for new talkbox setup page
def loadNewTBPage():
    	screen.fill((255, 255, 255))
	background.fill((255, 255, 255))
	background.blit(remixerTiny, (20,0))
	background.blit(inputIcon, (10, 140))
	background.blit(processIcon, (145, 130))
	background.blit(outputIcon, (305, 130))
	background.blit(processIcon, (145, 130))
	background.blit(newIconTiny, (180, 10))
	background.blit(rpiTiny, (350,5))
	screen.blit(background, (0,0))
	pygame.display.update()

#Load icons and background for talkbox operations page
def loadNewOperationPage():
   	screen.fill((255, 255, 255))
	background.fill((255, 255, 255))
	background.blit(remixerTiny, (20,0))
	background.blit(inputIcon, (10, 140))
	background.blit(outputIcon, (305, 130))
	background.blit(processIcon, (145, 130))
	background.blit(talkBoxTiny, (180, 0))
	background.blit(rpiTiny, (350,5))
	screen.blit(background, (0,0))
	pygame.display.update()
