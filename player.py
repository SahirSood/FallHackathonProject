import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
FPS = 60
WIDTH = 20
HEIGHT = 20

class Player(pygame.sprite.Sprite):
    WIDTH = 20
    HEIGHT = 20
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0) 
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -(ACC)
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC  

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > SCREEN_WIDTH - WIDTH:
            self.pos.x = SCREEN_WIDTH - WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
     
        self.rect.midbottom = self.pos
