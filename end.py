import pygame 

pygame.init() # also starts pygame font 

class End_Block(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft = pos)
    
    def display(x,y,z,w):
        x.blit(y,z,w)
        
    def update(self,x_shift):
        self.rect.x += x_shift
