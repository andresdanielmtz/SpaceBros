from tabnanny import check
from numpy import character
import pygame, sys
from settings import *
from level import Level, checkCollision 
from menu.button2 import Button
bg = pygame.image.load('graphics/space.png')
bg = pygame.transform.scale(bg, (1500, 1500)) # arbitrary parameters 

#setup
pygame.init() # also starts pygame font 

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("menu/font.ttf", size)

pygame.display.set_caption('Space Bros. & Sisters')
screen = pygame.display.set_mode((dsp_width,dsp_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(15).render("""For credits, bibliographic references and more, visit:""", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(650, 50))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(230, 650), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Yellow")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def game():
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('This is just as correct...', False, (255, 255, 255))
    
    screen.fill('black')
    screen.blit(bg, (0,0)) 
    screen.blit(text_surface, (0,0))
    level.run()
    pygame.display.update()
    clock.tick(60) 

def main_menu():
    while True:
        screen.blit(bg, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("JAMES WEBB TELESCOPE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("menu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("menu/Options Rect.png"), pos=(640, 400), 
                            text_input="CREDITS", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("menu/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "game"
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "options"
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
        
        screen.fill('black')
        screen.blit(bg, (0,0)) 
        screen.blit(text_surface, (0,0))
        level.run()
    elif x == "options":
        options()
    pygame.display.update()
    clock.tick(60) 