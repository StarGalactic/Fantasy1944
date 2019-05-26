import pygame, pyganim, random, math
from pygame.locals import *

class units(pygame.sprite.Sprite):
    def __init__(self, unitPrice, health, damage, speed):
        super().__init__()
        self.unitPrice = unitPrice
        self.health = health
        self.damage = damage
        self.speed = speed
        self.playerSpriteStartX = 30
        self.enemySpriteStartX = 1000


        betterKnightAtk = [('SpriteArt\\betterKnightAtk\\tile%s.png' % (str(num).rjust(3, '0')), 50) for num in range(62)]
        betterKnightWalk = [('SpriteArt\\betterKnightWalk\\tile%s.png' % (str(num).rjust(3, '0')), 50) for num in range(62)]
        wizardWalk = [('SpriteArt\\wizardWalk\\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range(62)]
        wizardAtk = [('SpriteArt\\wizardAtk\\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range(37)]
        goblinAnim = [('SpriteArt\GoblinWalk\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range (3)]

        WizAAnim = pyganim.PygAnimation(wizardAtk)
        WizWAnim = pyganim.PygAnimation(wizardWalk)

        self.walkAnimations = []
        self.walkAnimations.append(betterKnightWalk)
        self.walkAnimations.append(WizWAnim)
        print(self.walkAnimations)
        self.attackAnimations = []
        self.attackAnimations.append(betterKnightAtk)
        self.attackAnimations.append(WizAAnim)







class meleeUnit(units):
    def __init__(self, unitPrice, health, damage, speed):
        super().__init__(unitPrice, health, damage, speed)
        self.image = pygame.image.load("SpriteArt\\betterKnightAtk\\tile000.png")
        self.rect = self.image.get_rect()
        self.x = 30
        self.y = 640







'''class wizardUnit(units):
    def __init__(self):
        super().__init__(
            unitPrice=500,
            health = 150,
            damage=20,
            speed = 0.75
        )
'''
class enemyUnit(units):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.image = pygame.image.load("SpriteArt\\GoblinWalk\\tile000.png")
        self.rect = self.image.get_rect()
        self.x = 1000
        self.y = 640
