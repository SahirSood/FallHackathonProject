import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12
FPS = 60
gravity = 0.1


class Player(pygame.sprite.Sprite):
    WIDTH = 20
    HEIGHT = 20
    SCORE = 0
    jumpHeight = -12
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0.5) 
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -(ACC)
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        

        if self.pos.x > SCREEN_WIDTH - self.WIDTH:
            self.pos.x = SCREEN_WIDTH - self.WIDTH
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > SCREEN_HEIGHT - self.HEIGHT:
            self.pos.y = SCREEN_HEIGHT - self.HEIGHT
        if self.pos.y < 0:
            self.pos.y = 0
     
        self.rect.midbottom = self.pos

    def incrementScore(self):
        self.SCORE += 1        

    def jump(self):
        self.vel.y = self.jumpHeight
           
