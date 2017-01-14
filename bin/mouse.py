#This code was created by Foad Hamidi and modified by David Yin
#Version 1: November 2016

#This code handles point-click input on the talkbox interface

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import os
import time
from sys import exit
from pygame.locals import *
from pygame import Rect
from initTB import *

# Define mouse events
def mouseEvent(x,y):
    	if pygame.Rect(rpi_rect).collidepoint(x,y):
        	pygame.quit()
        	exit()
    	if pygame.Rect(rpiTiny_rect).collidepoint(x,y):
        	#os.system("starx")
        	pygame.quit()
        	exit()
    	if pygame.Rect(remixer_rect).collidepoint(x,y):
      		return 2
    	if pygame.Rect(remixerTiny_rect).collidepoint(x,y):
        	return 1
	if pygame.Rect(newIcon_rect).collidepoint(x,y):
        	return 5
	if pygame.Rect(talkBox_rect).collidepoint(x,y):
        	return 3
    	return 2
