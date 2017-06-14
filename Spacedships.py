#importing
import pygame
import random
from pygame.locals import *

#intializing
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
health = 20

#importing pictures
badshippic = pygame.image.load("resources/badship.png")
goodshippic = pygame.image.load("resources/goodship.png")

#transforming pictures
badship = pygame.transform.scale(badshippic,(64,64))
goodship = pygame.transform.scale(goodshippic,(64,64))

#the great loop
while True:
    badrect = pygame.Rect(badship.get_rect())
    goodrect = pygame.Rect(goodship.get_rect())
    
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
        goodrect.y += 1.5
    elif keys[2]:
        goodrect.y -= 1.5
    if keys[1]:
        goodrect[0]-=1.5
    elif keys[3]:
        goodrect[0]+=1.5

    badrect[1] +=0.5

#colliding party
    
    
    if badrect.colliderect(goodrect):
        health -= 5
        print(goodrect)

    
