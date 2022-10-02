import pygame 

#primary mirror 
class PrimaryMirror(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        # self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)

        self.image = pygame.image.load("telescope/info/1.png")
        self.image = pygame.transform.scale(self.image, (380, 567)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

#secondary 
class SecondaryMirror(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((2500, 720))
        # self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)

        self.image = pygame.image.load("telescope/info/2.png")
        self.image = pygame.transform.scale(self.image, (861, 242)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

class Sunshield(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)

        self.image = pygame.image.load("telescope/info/3.png")
        self.image = pygame.transform.scale(self.image, (400, 648)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

class ISIM(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
    
        self.image = pygame.image.load("telescope/info/4.png")
        self.image = pygame.transform.scale(self.image, (961, 246)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift
        
class MTT(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
    
        self.image = pygame.image.load("telescope/info/5.png")
        self.image = pygame.transform.scale(self.image, (1022, 242)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

class SpaceCraft(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
    
        self.image = pygame.image.load("telescope/info/6.png")
        self.image = pygame.transform.scale(self.image, (992, 540)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

class SolarPanel(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
    
        self.image = pygame.image.load("telescope/info/7.png")
        self.image = pygame.transform.scale(self.image, (960, 540)) # res/2 
    def update(self,x_shift):
        self.rect.x += x_shift

class HighGainAntenna(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.image.load("telescope/info/8.png")
    def update(self,x_shift):
        self.rect.x += x_shift
        
class StarTracker(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((1920, 1080))
        self.image.fill((171, 26, 19)) # red 
        #self.rect = self.image.get_rect(topleft = pos)
        self.image = pygame.image.load("telescope/info/9.png")
    def update(self,x_shift):
        self.rect.x += x_shift
        
        