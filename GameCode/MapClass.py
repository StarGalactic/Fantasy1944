import pygame, random
from pygame.locals import *
from pgu import gui

class lane:
    def __init__(self, mouseY, unit, currency, unitPrice):
        self.y = mouseY
        self.unit = unit
        self.goldCount = currency
        self.image = pygame.image.load("dogSprite.png").convert_alpha()


    def laneSelect(self, mouseY):
        if self.mouseY > "":


    def unitSpawn(self, unit, currency, unitPrice):
        if self.currency >= unitPrice:
            if self.unit == 1:
                screen.blit
