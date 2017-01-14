#This code was created by Foad Hamidi and modified by David Yin
#Version 1: November 2016

#This code sets the sound corresponding to the pins touched on the touch hat

import Adafruit_MPR121.MPR121 as MPR121
import pygame
import os
import time
from sys import exit
from pygame.locals import *
from pygame import Rect

MAX_SELECTION = 12

def fillSoundlist1():
    	scl = [None] * 12
	sl1 = [None] * 12
    	#Here we load the first set of sounds.
	if os.path.exists("../Sounds/Set1/S1.wav"):
		sound1 = pygame.mixer.Sound("../Sounds/Set1/S1.wav")
	else:
		sound1 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel1 = pygame.mixer.Channel(1)
	sl1[0] = sound1
	scl[0] = soundChannel1
	if os.path.exists("../Sounds/Set1/S2.wav"):
		sound2 = pygame.mixer.Sound("../Sounds/Set1/S2.wav")
	else:
		sound2 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel2 = pygame.mixer.Channel(2)
	sl1[1] = sound2
	scl[1] = soundChannel2
	if os.path.exists("../Sounds/Set1/S3.wav"):
		sound3 = pygame.mixer.Sound("../Sounds/Set1/S3.wav")
	else:
		sound3 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel3 = pygame.mixer.Channel(3)
	sl1[2] = sound3
	scl[2] = soundChannel3
	if os.path.exists("../Sounds/Set1/S4.wav"):
		sound4 = pygame.mixer.Sound("../Sounds/Set1/S4.wav")
	else:
		sound4 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel4 = pygame.mixer.Channel(4)
	sl1[3] = sound4
	scl[3] = soundChannel4
	if os.path.exists("../Sounds/Set1/S5.wav"):
		sound5 = pygame.mixer.Sound("../Sounds/Set1/S5.wav")
	else:
		sound5 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel5 = pygame.mixer.Channel(5)
	sl1[4] = sound5
	scl[4] = soundChannel5
	if os.path.exists("../Sounds/Set1/S6.wav"):
		sound6 = pygame.mixer.Sound("../Sounds/Set1/S6.wav")
	else:
		sound6 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel6 = pygame.mixer.Channel(6)
	sl1[5] = sound6
	scl[5] = soundChannel6
	if os.path.exists("../Sounds/Set1/S7.wav"):
		sound7 = pygame.mixer.Sound("../Sounds/Set1/S7.wav")
	else:
		sound7 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel7 = pygame.mixer.Channel(7)
	sl1[6] = sound7
	scl[6] = soundChannel7
	if os.path.exists("../Sounds/Set1/S8.wav"):
		sound8 = pygame.mixer.Sound("../Sounds/Set1/S8.wav")
	else:
		sound8 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel8 = pygame.mixer.Channel(1)
	sl1[7] = sound8
	scl[7] = soundChannel8
	if os.path.exists("../Sounds/Set1/S9.wav"):
		sound9 = pygame.mixer.Sound("../Sounds/Set1/S9.wav")
	else:
		sound9 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel9 = pygame.mixer.Channel(2)
	sl1[8] = sound9
	scl[8] = soundChannel9
	if os.path.exists("../Sounds/Set1/S10.wav"):
		sound10 = pygame.mixer.Sound("../Sounds/Set1/S10.wav")
	else:
		sound10 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel10 = pygame.mixer.Channel(3)
	sl1[9] = sound10
	scl[9] = soundChannel10
	if os.path.exists("../Sounds/Set1/S11.wav"):
		sound11 = pygame.mixer.Sound("../Sounds/Set1/S11.wav")
	else:
		sound11 = pygame.mixer.Sound("../Sounds/Silence.wav")
	soundChannel11 = pygame.mixer.Channel(4)
	sl1[10] = sound11
	scl[10] = soundChannel11
	sound12 = pygame.mixer.Sound("../Sounds/change.wav")
	soundChannel12 = pygame.mixer.Channel(5)
	sl1[11] = sound12
	scl[11] = soundChannel12
    	return sl1,scl

def fillSoundlist2():
    	sets = 1
    	sl2 = [None] * MAX_SELECTION
    	#Here we load the second set of sounds.
	if os.path.exists("../Sounds/Set2/S1.wav"):
		sets = 2
	if os.path.exists("../Sounds/Set2/S1.wav"):
		sound1B = pygame.mixer.Sound("../Sounds/Set2/S1.wav")
	else:
		sound1B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[0] = sound1B
	if os.path.exists("../Sounds/Set2/S2.wav"):
		sound2B = pygame.mixer.Sound("../Sounds/Set2/S2.wav")
	else:
		sound2B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[1] = sound2B
	if os.path.exists("../Sounds/Set2/S3.wav"):
		sound3B = pygame.mixer.Sound("../Sounds/Set2/S3.wav")
	else:
		sound3B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[2] = sound3B
	if os.path.exists("../Sounds/Set2/S4.wav"):
		sound4B = pygame.mixer.Sound("../Sounds/Set2/S4.wav")
	else:
		sound4B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[3] = sound4B
	if os.path.exists("../Sounds/Set2/S5.wav"):
		sound5B = pygame.mixer.Sound("../Sounds/Set2/S5.wav")
	else:
		sound5B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[4] = sound5B
	if os.path.exists("../Sounds/Set2/S6.wav"):
		sound6B = pygame.mixer.Sound("../Sounds/Set2/S6.wav")
	else:
		sound6B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[5] = sound6B
	if os.path.exists("../Sounds/Set2/S7.wav"):
		sound7B = pygame.mixer.Sound("../Sounds/Set2/S7.wav")
	else:
		sound7B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[6] = sound7B
	if os.path.exists("../Sounds/Set2/S8.wav"):
		sound8B = pygame.mixer.Sound("../Sounds/Set2/S8.wav")
	else:
		sound8B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[7] = sound8B
	if os.path.exists("../Sounds/Set2/S9.wav"):
		sound9B = pygame.mixer.Sound("../Sounds/Set2/S9.wav")
	else:
		sound9B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[8] = sound9B
	if os.path.exists("../Sounds/Set2/S10.wav"):
		sound10B = pygame.mixer.Sound("../Sounds/Set2/S10.wav")
	else:
		sound10B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[9] = sound10B
	if os.path.exists("../Sounds/Set2/S11.wav"):
		sound11B = pygame.mixer.Sound("../Sounds/Set2/S11.wav")
	else:
		sound11B = pygame.mixer.Sound("../Sounds/Silence.wav")
	sl2[10] = sound11B
	sound12B = pygame.mixer.Sound("../Sounds/change.wav")
	sl2[11] = sound12B
    	return sets,sl2
