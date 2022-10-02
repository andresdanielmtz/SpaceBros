import pygame
from PIL import Image, ImageSequence

def loadGIF(filename):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)
    return frames

class AnimatedSpriteObject(pygame.sprite.Sprite):
    def __init__(self, x, bottom, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom = (x, bottom))
        self.image_index = 0
    def update(self):
        self.image_index += 1
        self.image = self.images[self.image_index % len(self.images)]
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = pygame.display.get_surface().get_width()

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
        self.get_input()