#!/usr/bin/env python

#This code is developed by Foad Hamidi, 2016.
#This code was modified by David Yin.
#Version 1: November 2016

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import os
import time
from sys import exit
from pygame.locals import *
from pygame import Rect
from initTB import *
from pages import *
from mouse import *
from sounds import *

#Define constants for corresponding talkbox pages and sound selection
WELCOME_PAGE = 1
MAIN_PAGE = 2
TALK_BOX_PAGE = 3
OPERATION_PAGE = 4
NEW_TB_PAGE = 5
MAX_SELECTION = 12
SWITCH_SOUND = 11

#Initialize Variables
#Used to implemented interaction. We load TalkBox on start by loading page number 3.
pageNumber = TALK_BOX_PAGE
#We will have possibly two sets  of sound. This variable records which set is on.
currentSoundList = 1
numberOfSoundSets = 1

#pygame.mouse.set_visible(False)

#Main program loop
while True:

	# Operation page pin touch value
	if pageNumber == OPERATION_PAGE:
		current_touched = cap.touched()
		# Check each pin's last and current state to see if it was pressed or released.
		for i in range(MAX_SELECTION):
		# Each pin is represented by a bit in the touched value.  A value of 1
		# means the pin is being touched, and 0 means it is not being touched.
			pin_bit = 1 << i
			# First check if transitioned from not touched to touched.
			if current_touched & pin_bit and not last_touched & pin_bit:
				print '{0} touched!'.format(i)
				soundChannel = soundChannelList[i]
				if currentSoundList == 1:
                                        sound = soundList1[i]
                                elif currentSoundList == 2:
                                        sound = soundList2[i]
				soundChannel.play(sound)
                                #If it is the special 11th sound, switch to other set.
                                if i==SWITCH_SOUND:
                                        if currentSoundList == 2:
                                                currentSoundList = 1
                                                print'Set Switched to 1'
                                        elif currentSoundList == 1:
                                                if numberOfSoundSets==2:
                                                        currentSoundList = 2
                                                        print'Set Switched to 2'
				print'Sound played'
                                loadIcons()


                        # Next check if transitioned from touched to not touched.
                        if not current_touched & pin_bit and last_touched & pin_bit:
                                print '{0} released!'.format(i)
		# Update last state and wait a short period before repeating.
		last_touched = current_touched
		time.sleep(0.1)



        # eventListener
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        exit()
                #The start of the program
		elif pageNumber == WELCOME_PAGE:
			#Checking for user input
			if event.type == MOUSEBUTTONDOWN:
			#or event.type == MOUSEBUTTONUP:
				x, y = event.pos
				pageNumber = mouseEvent(x,y)
			loadWelcomePage()
	
		#The main page
		elif pageNumber == MAIN_PAGE:
			loadMainPage()

			if event.type == MOUSEBUTTONDOWN:
			# or event.type == MOUSEBUTTONUP:
                                x, y = event.pos
                                pageNumber = mouseEvent(x,y)

		#Operation page
		elif pageNumber == OPERATION_PAGE:
			if event.type == MOUSEBUTTONDOWN:
			# or event.type == MOUSEBUTTONUP:
				x, y = event.pos
				pageNumber = mouseEvent(x,y)

		#New talkbox project page
		elif pageNumber == NEW_TB_PAGE:
			loadNewTBPage()

                        if event.type == MOUSEBUTTONDOWN:
			# or event.type == MOUSEBUTTONUP:
                                x, y = event.pos
                                pageNumber = mouseEvent(x,y)

		#New talkbox operation page
		elif pageNumber == TALK_BOX_PAGE:
			loadNewOperationPage()

                        #We setup TalkBox here
                        cap = MPR121.MPR121()
                        if not cap.begin():
                                print 'Error initializing MPR121.  Check your wiring!'
                                sys.exit(1)

                        #Initalize and load the sound module.
                        pygame.mixer.init(48000, -16, 1, 1024)
                        soundChannelList = [None] * MAX_SELECTION
                        soundList1 = [None] * MAX_SELECTION
                        soundList2 = [None] * MAX_SELECTION

                        #Generate Soundlists
                        soundList1, soundChannelList = fillSoundlist1()
                        numberOfSoundSets, soundList2 = fillSoundlist2()

                        print "Soundboard Ready."
                        pageNumber = OPERATION_PAGE
                        last_touched = cap.touched()
