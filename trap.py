import pygame
import random
import player
import os

vec = pygame.math.Vector2

class Trap:
    def __init__(self):
        self.HEIGHT = 20
        self.WIDTH = random.randint(100, 200)
        self.pos = vec(player.SCREEN_WIDTH, player.SCREEN_HEIGHT - self.HEIGHT)
        self.image = pygame.image.load(os.path.join(os.path.join('icon', 'spill.png'))) #change with wings image

    def move(self):
        self.pos  -= vec(1, 0)

    def collide(self, p):
        oRect = pygame.Rect(self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT)
        pRect = pygame.Rect(p.pos[0], p.pos[1], p.WIDTH, p.HEIGHT)
        if oRect.colliderect(pRect):
            p.vel.y = 0
            p.acc.y = 0
        else:
            self.acc = vec(0,0.5) 
    
    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        screen.blit(self.image, (self.pos.x, self.pos.y))