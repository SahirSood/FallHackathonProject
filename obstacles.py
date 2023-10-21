from pygame.locals import *
import pygame
import player
import random

vec = pygame.math.Vector2

class Obstacles(pygame.sprite.Sprite):
    
    
    def __init__(self):
        super().__init__() 
        self.HEIGHT = random.randint(5, 80)
        self.WIDTH = random.randint(5, 10)
        self.pos = vec(player.SCREEN_WIDTH, player.SCREEN_HEIGHT - self.HEIGHT)       

    def move(self):
        self.pos -= vec(2, 0)

    def collide(self, p):
        oRect = pygame.Rect(self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT)
        pRect = pygame.Rect(p.pos[0], p.pos[1], p.WIDTH, p.HEIGHT)
        if oRect.colliderect(pRect):
            return True
        return False
