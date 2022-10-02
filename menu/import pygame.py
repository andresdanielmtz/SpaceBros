import pygame              #Aqui se importa la libreria de pygame
from sys import exit     #Esto es para que no salga error en el programan 

pygame.init()            #Iniciar todo
screen = pygame.display.set_mode((800,400)) #Crear Pantalla
pygame.display.set_caption('NASA')      #Nombre del juego
clock = pygame.time.Clock()        #Aqui es para poner a cuantoa fps va correr

sky_surface = pygame.image.load('f2.png')   #Poner fondo de png
ground_surface = pygame.image.load('tierra.png')


while True:                              #Para que siempre se ejecute
    for event in pygame.event.get():    #Aqui nos despliega todos las escenas
        if event.type == pygame.QUIT:     #Este es el boton de x
            pygame.quit()                #Despues de esto ya no se puede hacer nada
            exit()                        #Esto es para que no salga error en el programan 

    screen.blit(sky_surface,(0,0))           #Aqui es para mover el color del fondo

    pygame.display.update()      #Para que se depliegue en la pantalla 
    clock.tick(60)              #Aqui es para poner a cuantoa fps va correr



