import pygame 

#primary mirror 
class PrimaryMirror(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        # self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)

        self.image = pygame.image.load("telescope/info/1.png")
        self.image = pygame.transform.scale(self.image, (960, 540)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift
