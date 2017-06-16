#importing
import pygame
import random
import time
from pygame.locals import *

#intializing
pygame.init()
width, height = 850, 720
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
health = 20
shooting = 0
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]

#importing pictures
badshippic = pygame.image.load("resources/badship.png")
goodshippic = pygame.image.load("resources/goodship.png")
bombpic = pygame.image.load("resources/cannonball_2.png")

#transforming pictures
badship = pygame.transform.scale(badshippic,(64,64))
goodship = pygame.transform.scale(goodshippic,(64,64))
bomb = pygame.transform.scale(bombpic,(64,64))

#get rekt m8
badrect = pygame.Rect(badship.get_rect())
goodrect = pygame.Rect(goodship.get_rect())
bombrect = pygame.Rect(bomb.get_rect())
goodrect.x, goodrect.y = [425,650]
bombrect.x, goodrect.y = [goodrect.x,goodrect.y]


#the great loop
while True:
    screen.fill(0)
    screen.blit(badship, (badrect.x, badrect.y))
    screen.blit(goodship, (goodrect.x,goodrect.y))
    pygame.display.flip()

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
        goodrect.y -= 1.5
    elif keys[2]:
        goodrect.y += 1.5
    if keys[1]:
        goodrect.x -= 1.5
    elif keys[3]:
        goodrect.x += 1.5

    badrect.y += 1
    bombrect.y -= 2
#colliding party
    if badrect.colliderect(goodrect):
        health -= 1

#badboys, badboys, what you gonna do?
    badtimer -= 1
    if badtimer == 0:
        badguys.append([random.randint(64, 786),64])
        badtimer = 100-(badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

        index = 0
        for badguy in badguys:
            if badguy[0] < -64:
                badguys.pop(index)
            badguy[0] -= 7
            index += 1
        for badguy in badguys:
            screen.blit(badship, badguy)

    print(pygame.mouse.get_pos())
            

        
        
        
    
