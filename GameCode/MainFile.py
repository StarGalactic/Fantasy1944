import os, random, pygame, math, sys, pyganim
from UnitClass import *
from MapClass import *
'''------------------------------Screen Def----------------------------'''
os.environ["SDL_VIDEO_CENTERED"] = "1"
length_x = 1024
width_y = 1024
screen = pygame.display.set_mode((length_x, width_y))
pygame.display.set_caption("Fantasy 1944")

'''----------------------------- Function Def -------------------------'''

'''----------------------------- Color Def ----------------------------'''
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIME = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
MAGENTA = (255,0,255)
SILVER = (192,192,192)
GREY = (128,128,128)
MAROON = (128,0,0)
OLIVE = (128,128,0)
GREEN = (0,128,0)
PURPLE = (128,0,128)
TEAL = (0,128,128)
NAVY = (0,0,128)
GREEN = (0, 128, 0)
BROWN = (64, 32, 6)


color_list = [BLACK, WHITE, RED, LIME, BLUE, YELLOW, AQUA, MAGENTA, SILVER, GREY, MAROON, OLIVE, GREEN, PURPLE, TEAL, NAVY, GREEN, BROWN]

'''------------------------------Global def----------------------------'''
background = pygame.image.load("SpriteArt\Background(fix).png").convert_alpha()
x = 30

level = 0
currency = 0
melee = ''
clock  = pygame.time.Clock()


allSprites = pygame.sprite.Group()
meleeSprites = pygame.sprite.Group()
wizardSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()

'''------------------------------Pyganim Load--------------------------'''
betterKnightAtk = [('SpriteArt\\betterKnightAtk\\tile%s.png' % (str(num).rjust(3, '0')), 50) for num in range(62)]
betterKnightWalk = [('SpriteArt\\betterKnightWalk\\tile%s.png' % (str(num).rjust(3, '0')), 50) for num in range(62)]
wizardWalk = [('SpriteArt\\wizardWalk\\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range(62)]
wizardAtk = [('SpriteArt\\wizardAtk\\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range(37)]
goblinMovement = [('SpriteArt\\GoblinWalk\\tile%s.png' % (str(num).rjust(3, '0')), 100) for num in range (2)]
BKAAnim = pyganim.PygAnimation(betterKnightAtk)
BKWAnim =pyganim.PygAnimation(betterKnightWalk)
WizAAnim = pyganim.PygAnimation(wizardAtk)
WizWAnim = pyganim.PygAnimation(wizardWalk)
goblinAnim = pyganim.PygAnimation(goblinMovement)

'''------------------------------Main Loop ----------------------------'''
BackGround = Background('SpriteArt\\BackgroundFull.png', [0,0])
running = True
while running:
    p = meleeUnit(300, 400, random.randint(40, 60), 5)
    e = enemyUnit(self, 200, random.randint(20,65), 7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_1:
                melee = True
            elif event.key == pygame.K_2:
                melee = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if melee == True:

                    allSprites.add(s)
                    meleeSprites.add(s)
                elif melee == False:
                    l  = wizardUnit()
                    allSprites.add(l)
                    wizardSprites.add(l)


    for s in meleeSprites:
        while s.health > 0:
            walking = True
            BKWAnim.play()
            BKWAnim.blit(screen, (x, 640))
            pygame.display.update()
            timer = pygame.time.get_ticks() # outputs from time started in milisec

            if timer % 100 == 0 and walking == True:
                x += s.speed #self.speed
                screen.blit(BackGround.image, BackGround.rect)
                pygame.display.update()

            if pygame.sprite.collide_rect(p.rect, e.rect) == True:
                BKWAnim.stop()
                walking = False
                BKAAnim.play()
                BKAAnim.blit(screen, ())
                e.health -= p.damage
                p.health -= e.damage

        if s.health <= 0:
            BKWAnim.stop()
            allSprites.remove(s)
            playerSprites.remove(s)

    if level == 0:
        currency = 300
        for k in allSprites:
            if x> 1024:
                level += 1

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    pygame.display.update()




    clock.tick(60)

    pygame.display.flip()
