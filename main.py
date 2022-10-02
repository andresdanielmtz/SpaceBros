from tabnanny import check
from numpy import character
import pygame, sys
from settings import *
from level import Level, checkCollision 
from menu.button2 import Button

bg = pygame.image.load('graphics/space.png')
bg = pygame.transform.scale(bg, (1500, 1500)) # arbitrary parameters 
bg_menu = pygame.image.load('graphics/main.png')
bg_menu = pygame.transform.scale(bg_menu, (1450,1450))
qr = pygame.image.load("graphics/space_craft_bus.png")
qr = pygame.transform.scale(qr, (1450, 900))
#setup
pygame.init() # also starts pygame font 

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("menu/font.ttf", size)

d_width = 1450
d_height = 900 

pygame.display.set_caption('Space Bros. & Sisters')
screen = pygame.display.set_mode((d_width,d_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
value_score = 0 


def game():
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    # text_surface = my_font.render('This is just as correct...', False, (255, 255, 255))
    
    screen.fill('black')
    screen.blit(bg, (0,0)) 
    # screen.blit(text_surface, (0,0))
    level.run()
    pygame.display.update()
    clock.tick(60) 

def main_menu():
    while True:
        screen.blit(bg_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("JAMES WEBB TELESCOPE", True, "#d7fcd4")
        MENU_RECT = MENU_TEXT.get_rect(center=((d_width / 2), 100))

        PLAY_BUTTON = Button(image=pygame.image.load("menu/Play Rect.png"), pos=((d_width / 2), 425), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("menu/Quit Rect.png"), pos=((d_width / 2), 550), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        # reference = Button(image=pygame.image.load("menu/options2.png"), pos=(640, 400),
                            # text_input="Settings", font=get_font(30), base_color = "#d7fcd4", hovering_color="White" )
        

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "game"
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
#Running
x = main_menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if x == "game": 
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('This is just as correct...', False, (255, 255, 255))
        # score = my_font.render('Score: '+str(level.value_score), False, (255, 255, 255))
        
        screen.fill('black')
        screen.blit(bg, (0,0)) 
        # screen.blit(text_surface, (0,0))
        # screen.blit(score,((dsp_width/2), 0))
        screen.blit(level.score,((dsp_width/2), 890))
        level.run()
        if level.state: 
            screen.blit(qr, (0,0) )
        '''if level.state: 
            screen.blit()
            print("IT IS WORKING GUYSSS")'''

    pygame.display.update()
    clock.tick(60)  