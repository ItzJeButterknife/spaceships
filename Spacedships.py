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
randomx = []
index = 0
clock = pygame.time.Clock()

#importing pictures
badshippic = pygame.image.load("resources/badship.png")
goodshippic = pygame.image.load("resources/goodship.png")
bombpic = pygame.image.load("resources/cannonball_2.png")
heartpic = pygame.image.load("resources/hearts.png")

#transforming pictures
badship = pygame.transform.scale(badshippic,(64,64))
goodship = pygame.transform.scale(goodshippic,(64,64))
bomb = pygame.transform.scale(bombpic,(64,64))
heart = pygame.transform.scale(heartpic,(26,25))

#get rekt m8
goodrect = pygame.Rect(goodship.get_rect())
bombrect = pygame.Rect(bomb.get_rect())
goodrect.x, goodrect.y = [425,650]
bombrect.x, goodrect.y = [goodrect.x,goodrect.y]

#the badboy
class badboy():
    def __init__(self, x, y, image):
        global index
        self.image = image
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.x = x
        self.rect.y = y
        badguys.append(self)
        screen.blit(image,(self.rect.x,self.rect.y))

#something to say?
##def message(text, color):
##    text = pygame.font.Font('resources/impact.ttf', 115)
##    surface = font.render(text, True, color)
##    textplace = ((width/2),(height/2))
##    screen.blit(surface, textplace)
    
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
    x = random.randrange(0,786)
    randomx.append(x)
    y = random.randrange(-500,-64)
    for i in range(0,15):
        i = badboy(randomx[random.randint(0,len(randomx)-1)], y, badship)
        index += 1
        if len(badguys) >= 10:
            badguys.pop(len(badguys)-1)
        
#colliding party
    index = 0
    for badguy in badguys:
        badguy.rect.y += 3
        screen.blit(badship,(badguy.rect.x,badguy.rect.y))
        if badguy.rect.colliderect(goodrect):
            badguys.pop(index)
            health -= 1
        if badguy.rect.y >= 730:
            badguys.pop(index)
        index += 1

#Stay healthy!  
    if health == 3:
        screen.blit(heart,(5,5))
        screen.blit(heart,(55,5))
        screen.blit(heart,(105,5))
    elif health == 2:
        screen.blit(heart,(5,5))
        screen.blit(heart,(55,5))
    elif health == 1:
        screen.blit(heart,(5,5))
    elif health <= 0:
        #message("Game over!", (255,0,0))
        pygame.quit()
        quit()

#draw me like one of your french girl
    screen.blit(goodship, (goodrect.x,goodrect.y))
    pygame.display.flip()
    screen.fill(0)
    print(index)
