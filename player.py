import pygame
from pygame.locals import *
import main


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = main.vec((10, 385))
        self.vel = main.vec(0,0)
        self.acc = main.vec(0,0)

    def move(self):
        self.acc = main.vec(0,0) 
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -(main.ACC)
        if pressed_keys[K_RIGHT]:
            self.acc.x = main.ACC  

        self.acc.x += self.vel.x * main.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > main.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = main.WIDTH
     
        self.rect.midbottom = self.pos
