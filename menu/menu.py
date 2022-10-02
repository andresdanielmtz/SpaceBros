import pygame   
import button

pygame.init()

#Create a game window
SCREEN_WIDTH = 800
SCREEEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False 

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("menu/resume2.png").convert_alpha()
options_img = pygame.image.load("menu/options2.png").convert_alpha()
quit_img = pygame.image.load("menu/quit3.png").convert_alpha()


#create button instances
resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#game loop
run = True
while run:
    screen.fill((52, 78, 91))

    #check if game is paused 
    if game_paused == True:
        if resume_button.draw(screen):
            game_paused = False
        if options_button.draw(screen):
            pass
        if quit_button.draw(screen):
            run = False
        
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
