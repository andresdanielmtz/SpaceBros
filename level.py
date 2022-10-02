from multiprocessing import Barrier
from re import X
import pygame
from player import Player
from tiles import Tile
from collectible import Collectible
from barrier import Barrier
from end import End_Block 
from settings import tile_size, dsp_width, dsp_height
import asyncio 
import sys 

async def counter(): 
    print("lol")
    await asyncio.sleep(2)#seconds 
    print(":D")
    await asyncio.sleep(2)

def checkCollision():
    if pygame.sprite.spritecollideany(Player, Tile) != None:
        print('collision')
        return True
    return False
pygame.init()
value = 0
real_score = 0 
my_font = pygame.font.SysFont('Comic Sans MS', 30)

class Level:
    def __init__ (self,level_data,surface):
        #Setup de niveles
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.value_score = 0
        self.score = my_font.render('ALGO ASI', False, (255, 255, 255))

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.collectible = pygame.sprite.Group()
        self.barrier = pygame.sprite.Group()
        self.final = pygame.sprite.Group() 
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'x':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite= Player((x,y))
                    self.player.add(player_sprite)
                if cell == "v":
                    special = Collectible((x,y), tile_size)
                    self.collectible.add(special)
                if cell == "O":
                    barrera = Barrier((x,y), tile_size )
                    self.barrier.add(barrera)
                if cell == "f":
                    f_block = End_Block((x,y), tile_size)
                    self.final.add(f_block) # :D
                if cell == "H":
                    hana = Collectible((x,y), tile_size)
                    self.collectible.add(hana)
                if cell == "D": 
                    dul = Collectible((x,y), tile_size)
                    self.collectible.add(dul)
                if cell == "S":
                    ses = Collectible((x,y), tile_size)
                    self.collectible.add(ses)
                if cell == "N":
                    net = Collectible((x,y), tile_size)
                    self.collectible.add(net)
                if cell == "Y":
                    yeoseot = Collectible((x,y), tile_size)
                    self.collectible.add(yeoseot)
                if cell == "A":
                    daseot = Collectible((x,y), tile_size)
                    self.collectible.add(daseot)
                if cell == "I":
                    ilgob = Collectible((x,y), tile_size)
                    self.collectible.add(ilgob)
                
    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < dsp_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > dsp_width - (dsp_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
        
    def horizontal(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        
        for sprite in self.collectible.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.barrier.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        for sprite in self.final.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical(self):
        player = self.player.sprite
        player.apply_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 :
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.collectible.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 :
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
        for sprite in self.final.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 :
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0



                    #print(":D")
                    # self.add_points()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    #print("Don't.. hit it from the bottom!")
                global value 
                global real_score 
                value += 1
                if 10 <= value <= 30: 
                    real_score += 1
                    print(real_score)
                    value = 0 
                if real_score >= 10:
                    pass
                    #pygame.quit()
                    #sys.exit()
                #print(value)
        for sprite in self.barrier.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 :
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
        for sprite in self.final.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0 :
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        #Casillas De Nivel
        
        self.collectible.update(self.world_shift)
        self.collectible.draw(self.display_surface)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.barrier.update(self.world_shift)
        self.barrier.draw(self.display_surface)
        self.final.update(self.world_shift)
        self.final.draw(self.display_surface)
        self.scroll_x()
        #Jugador
        self.player.update()
        self.horizontal()
        self.vertical()
        self.player.draw(self.display_surface)
