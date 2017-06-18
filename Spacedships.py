#importing
import pygame
import random
from pygame.locals import *

#intializing
pygame.init()
width, height = 850, 720
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
health = 3
shooting = 0
badtimer = 100
badtimer1 = 0
badguys = []
clock = pygame.time.Clock()

#importing pictures
badshippic = pygame.image.load("resources/badship.png")
goodshippic = pygame.image.load("resources/goodship.png")
bombpic = pygame.image.load("resources/cannonball_2.png")

#transforming pictures
badship = pygame.transform.scale(badshippic,(64,64))
goodship = pygame.transform.scale(goodshippic,(64,64))
bomb = pygame.transform.scale(bombpic,(64,64))

#get rekt m8
goodrect = pygame.Rect(goodship.get_rect())
bombrect = pygame.Rect(bomb.get_rect())
goodrect.x, goodrect.y = [425,650]
bombrect.x, goodrect.y = [goodrect.x,goodrect.y]

class badguy():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.x = x
        self.rect.y = y
        badguys.append(self)

#the great loop
while True:
    clock.tick(60)

#key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
                elif event.key==K_SPACE:
                    screen.blit(bomb, (bombrect.x, bombrect.y))
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

#moving
    if keys[0]:
        goodrect.y -= 2.5
    elif keys[2]:
        goodrect.y += 2.5
    if keys[1]:
        goodrect.x -= 2.5
    elif keys[3]:
        goodrect.x += 2.5

    #badguyrect.y += 1
    bombrect.y -= 2

#badboys, badboys, what you gonna do?
    x = 0 #random.randrange(0,786)
    y = 0 #random.randrange(50,60)
    for i in range(0,10):
        i = badguy(x, y, badship)
        x += 50
        y += 50

    #colliding party
    for badguy in badguys:
        #badguy.y += 1
        if badguy.rect.colliderect(goodrect):
            health -= 1
            print("fuck")
    
    screen.blit(goodship, (goodrect.x,goodrect.y))
    pygame.display.flip()
    screen.fill(0)
