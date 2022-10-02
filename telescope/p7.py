import pygame 

#primary mirror 
class SolarPanel(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift
        