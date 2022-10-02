from tabnanny import check
from numpy import character
import pygame, sys
from settings import *
from level import Level, checkCollision 


bg = pygame.image.load('REAL/graphics/space.png')
bg = pygame.transform.scale(bg, (1500, 1500)) # arbitrary parameters 

#Setup principal
pygame.init()

pygame.display.set_caption('The James Webb Telescope')
screen = pygame.display.set_mode((dsp_width,dsp_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

#Running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('This is just as correct...', False, (255, 255, 255))
    

    screen.fill('black')
    screen.blit(bg, (0,0)) 
    screen.blit(text_surface, (0,0))
    level.run()
    pygame.display.update()
    clock.tick(60) 