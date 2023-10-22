from pygame.locals import *
import pygame
import player
import random
import os

vec = pygame.math.Vector2

class Obstacles(pygame.sprite.Sprite):
    
    def __init__(self, floating):
        super().__init__() 

        

        self.HEIGHT = 80
        self.WIDTH = 10
        if floating:
            self.pos = vec(player.SCREEN_WIDTH, random.randint(5, player.SCREEN_HEIGHT - self.HEIGHT)) 
            self.image = pygame.image.load(os.path.join('beer.png')) #change with wings
        else:
            self.pos = vec(player.SCREEN_WIDTH, player.SCREEN_HEIGHT - self.HEIGHT) 
            self.image = pygame.image.load(os.path.join('beer.png'))

    def move(self):
        self.pos -= vec(2, 0)

    def collide(self, p):
        oRect = pygame.Rect(self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT)
        pRect = pygame.Rect(p.pos[0], p.pos[1], p.WIDTH, p.HEIGHT)
        if oRect.colliderect(pRect):
            return True
        return False
    
    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (30, 30))
        screen.blit(self.image, (self.pos.x - 2 * self.HEIGHT, self.pos.y - 2 * self.HEIGHT))
