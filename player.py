import pygame
from PIL import Image, ImageSequence

lst = ["graphics/sprites/player/idle/1.png", "graphics/sprites/player/idle/2.png", "graphics/sprites/player/idle/3.png", "graphics/sprites/player/idle/4.png", "graphics/sprites/player/idle/5.png", "graphics/sprites/player/idle/6.png"]
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64)) # arbitrary parameter 
        self.image.fill('red')
        for elem in lst: 
            self.image = pygame.image.load(elem)
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            
            self.image = pygame.Surface((32,64))
            self.image = pygame.image.load("graphics/sprites/player/placeholders/Astronaut_Run.png")
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.Surface((32,64))
            self.image = pygame.image.load("graphics/sprites/player/placeholders/astro.png")
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
    def update(self):
        print("x:",self.rect.x) 
        print("y:",self.rect.y)

        # 680 
        if self.rect.y >= 924:
            self.rect.y = 20
            self.rect.x = 332 
        # x = 332
        # y = 680 
        
        #924 should be y limit 
        self.get_input()