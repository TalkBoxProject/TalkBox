#!/usr/bin/env python

#This code is developed by Foad Hamidi, 2016.

#First, we include the location of all the images we will be using:
remixer_image_filename = '../Media/remixer.jpg'
rpi_image_filename = '../Media/rpi.png'
newIcon_image_filename = '../Media/newIcon.png'
talkBox_image_filename = '../Media/talkbox.jpg'
remixerTiny_image_filename = '../Media/remixerTiny.jpg'
rpiTiny_image_filename = '../Media/rpiTiny.jpg'
talkBoxTiny_image_filename = '../Media/talkBoxTiny.jpg'
inputIcon_image_filename = '../Media/inputIcon.jpg'
processIcon_image_filename = '../Media/processIcon.jpg'
outputIcon_image_filename = '../Media/outputIcon.jpg'
newIconTiny_image_filename = '../Media/newIconTiny.png'
processIconOn_image_filename = '../Media/processIconOn.jpg'
outputIconOn_image_filename = '../Media/outputIconOn.jpg'
inputIconOn_image_filename = '../Media/inputIconOn.jpg'


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

pygame.init()

#Initializing the screen using dimensions of 3.5inch TFT Resistive Touchscreen
screen = pygame.display.set_mode((480, 320), 0, 32) #pygame.FULLSCREEN, 32)
screen.fill((255, 255, 255))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))
pygame.display.set_caption("reMixer")

#Loading all the needed image files
remixer = pygame.image.load(remixer_image_filename).convert()
rpi = pygame.image.load(rpi_image_filename).convert_alpha()
remixerTiny = pygame.image.load(remixerTiny_image_filename).convert()
rpiTiny = pygame.image.load(rpiTiny_image_filename).convert()
talkBox = pygame.image.load(talkBox_image_filename).convert()
newIcon = pygame.image.load(newIcon_image_filename).convert_alpha() 
talkBoxTiny = pygame.image.load(talkBoxTiny_image_filename).convert()
inputIcon = pygame.image.load(inputIcon_image_filename).convert_alpha()
processIcon = pygame.image.load(processIcon_image_filename).convert_alpha()
outputIcon = pygame.image.load(outputIcon_image_filename).convert_alpha()
newIconTiny = pygame.image.load(newIconTiny_image_filename).convert_alpha()
processIconOn = pygame.image.load(processIconOn_image_filename).convert_alpha()
outputIconOn = pygame.image.load(outputIconOn_image_filename).convert_alpha()
inputIconOn = pygame.image.load(inputIconOn_image_filename).convert_alpha()

#Creating rectangles for all the images to detect touch input
remixer_rect = pygame.Rect(5,20,250,240)
rpi_rect = pygame.Rect(220,28,250,221)
remixerTiny_rect = pygame.Rect(20, 0, 100, 113)
rpiTiny_rect = pygame.Rect(350, 0, 100, 88)
talkBox_rect = pygame.Rect(280, 110, 200, 200)
newIcon_rect = pygame.Rect(10, 130, 210, 168)

#Used to implemented interaction. We load TalkBox on start by loading page number 3.

pageNumber = 3

#pygame.mouse.set_visible(False)

#Main program loop
while True:

	if pageNumber == 4:
		current_touched = cap.touched()
		# Check each pin's last and current state to see if it was pressed or released.
		for i in range(12):	
		# Each pin is represented by a bit in the touched value.  A value of 1
 		# means the pin is being touched, and 0 means it is not being touched.
			pin_bit = 1 << i
                        # First check if transitioned from not touched to touched.
			if current_touched & pin_bit and not last_touched & pin_bit:
				print '{0} touched!'.format(i)
				soundChannel = soundChannelList[i-1]
				sound = soundList[i-1]
				soundChannel.play(sound)
				print'Sound played'
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


			# Next check if transitioned from touched to not touched.
			if not current_touched & pin_bit and last_touched & pin_bit:
				print '{0} released!'.format(i)
		# Update last state and wait a short period before repeating.
 		last_touched = current_touched
		time.sleep(0.1)


        
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
		#The start of the program
		elif pageNumber == 1:
			#Checking for user input
			if event.type == MOUSEBUTTONDOWN: 
			#or event.type == MOUSEBUTTONUP: 
				x, y = event.pos
				if pygame.Rect(rpi_rect).collidepoint(x,y): 
					pygame.quit()
					exit()
				if pygame.Rect(remixer_rect).collidepoint(x,y):
					pageNumber = 2
			#Initial interface is loaded
			screen.fill((255, 255, 255))
			background.fill((255, 255, 255))
        		background.blit(remixer, (5,20))
			background.blit(rpi, (220,28))
			screen.blit(background, (0,0))
			pygame.display.update()
		#The second screen
		elif pageNumber == 2:
			screen.fill((255, 255, 255))
			background.fill((255, 255, 255))
			background.blit(remixerTiny, (20,0))
			background.blit(newIcon, (10, 130)) 
			background.blit(talkBox, (280, 110))
                        background.blit(rpiTiny, (350,5))
			screen.blit(background, (0,0))
                        pygame.display.update()

			if event.type == MOUSEBUTTONDOWN:
			# or event.type == MOUSEBUTTONUP:
                               x, y = event.pos
                               if pygame.Rect(rpiTiny_rect).collidepoint(x,y):
                                       os.system("starx")
				       pygame.quit()
                                       exit()
                               if pygame.Rect(remixerTiny_rect).collidepoint(x,y):
                                       pageNumber = 1
                               if pygame.Rect(newIcon_rect).collidepoint(x,y):
                                       pageNumber = 5
                               if pygame.Rect(talkBox_rect).collidepoint(x,y):
                                       pageNumber = 3  
		elif pageNumber == 4:
                       if event.type == MOUSEBUTTONDOWN:
                       # or event.type == MOUSEBUTTONUP:
                               x, y = event.pos
                               if pygame.Rect(rpiTiny_rect).collidepoint(x,y):
                                       pygame.quit()
                                       exit()
                               if pygame.Rect(remixerTiny_rect).collidepoint(x,y):
                                       pageNumber = 2
                               if pygame.Rect(newIcon_rect).collidepoint(x,y):
                                       print 'newIcon'
                               if pygame.Rect(talkBox_rect).collidepoint(x,y):
                                       pageNumber = 2
                #New project page
		elif pageNumber == 5:
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

                        if event.type == MOUSEBUTTONDOWN:
                        # or event.type == MOUSEBUTTONUP:
                               x, y = event.pos
                               if pygame.Rect(rpiTiny_rect).collidepoint(x,y):
                                       pygame.quit()
                                       exit()
                               if pygame.Rect(remixerTiny_rect).collidepoint(x,y):
                                       pageNumber = 2
                               if pygame.Rect(newIcon_rect).collidepoint(x,y):
                                       print 'newIcon'
                               if pygame.Rect(talkBox_rect).collidepoint(x,y):
                                       pageNumber = 2

		elif pageNumber == 3:
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
                       
                       #We setup TalkBox here
                       cap = MPR121.MPR121()
                       if not cap.begin():
                       	   print 'Error initializing MPR121.  Check your wiring!'
                       	   sys.exit(1)

                       #Initalize and load the sound module.
                       pygame.mixer.init(48000, -16, 1, 1024)
                       soundChannelList = [None] * 12
                       soundList = [None] * 12

                       sound1 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S1.wav")
                       soundChannel1 = pygame.mixer.Channel(1)
                       soundList[0] = sound1
                       soundChannelList[0] = soundChannel1
                       sound2 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S2.wav")
                       soundChannel2 = pygame.mixer.Channel(2)
                       soundList[1] = sound2
                       soundChannelList[1] = soundChannel2
                       sound3 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S3.wav")
                       soundChannel3 = pygame.mixer.Channel(3)
                       soundList[2] = sound3
                       soundChannelList[2] = soundChannel3	
		       sound4 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S4.wav")
                       soundChannel4 = pygame.mixer.Channel(4)
                       soundList[3] = sound4
                       soundChannelList[3] = soundChannel4
                       sound5 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S5.wav")
                       soundChannel5 = pygame.mixer.Channel(5)
                       soundList[4] = sound5
                       soundChannelList[4] = soundChannel5
                       sound6 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S6.wav")
                       soundChannel6 = pygame.mixer.Channel(6)
                       soundList[5] = sound6
                       soundChannelList[5] = soundChannel6
                       sound7 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S7.wav")
                       soundChannel7 = pygame.mixer.Channel(7)
                       soundList[6] = sound7
                       soundChannelList[6] = soundChannel7
                       sound8 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S8.wav")
                       soundChannel8 = pygame.mixer.Channel(1)
                       soundList[7] = sound8
                       soundChannelList[7] = soundChannel8
                       sound9 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S9.wav")
                       soundChannel9 = pygame.mixer.Channel(2)
                       soundList[8] = sound9
                       soundChannelList[8] = soundChannel9
                       sound10 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S10.wav")
                       soundChannel10 = pygame.mixer.Channel(3)
                       soundList[9] = sound10
                       soundChannelList[9] = soundChannel10
                       sound11 = pygame.mixer.Sound("/home/pi/Foad/Sounds/Set1/S11.wav")
                       soundChannel11 = pygame.mixer.Channel(4)
                       soundList[10] = sound11
                       soundChannelList[10] = soundChannel11
                       sound12 = pygame.mixer.Sound("/home/pi/Foad/Sounds/sunny.wav")
                       soundChannel12 = pygame.mixer.Channel(5)
                       soundList[11] = sound12
                       soundChannelList[11] = soundChannel12
                       print "Soundboard Ready."
		       pageNumber = 4
                       last_touched = cap.touched() 
