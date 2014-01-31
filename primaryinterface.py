import sys, pygame
import serial
import pygame.mixer
from pygame.locals import *

class PrimaryInterface:
    def __init__(self, serial):
        pygame.init()
        pygame.display.set_mode((120, 120), DOUBLEBUF | HWSURFACE)

        self.serial = serial


    """Read from RFID reader and return rfid if found"""
    def read(self):
        self.serial.flushInput()
        rfid = self.serial.read(24)
        return rfid

    """Play sound file and return sound object"""
    def play(self, sound_file):
        sound = pygame.mixer.Sound("sounds/"+sound_file)
        sound.play(loops = -1)
        return sound

    """Stop playing sound object"""
    def stop(self, sound):
        if sound is not None:
            sound.stop()