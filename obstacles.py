from pygame.locals import *
import pygame
#from pygame.sprite import _Group
import player
import random
import os

vec = pygame.math.Vector2

class Obstacles(pygame.sprite.Sprite):
    
    def __init__(self, floating):
        super().__init__() 

        self.HEIGHT = 30
        self.WIDTH = 30
        if floating:
            self.pos = vec(player.SCREEN_WIDTH, random.randint(5, player.SCREEN_HEIGHT - self.HEIGHT)) 
            self.image = pygame.image.load(os.path.join('beer.png')) #change with wings image
        else:
            self.pos = vec(player.SCREEN_WIDTH, player.SCREEN_HEIGHT - self.HEIGHT) 
            self.image = pygame.image.load(os.path.join('beer.png'))

        (self.imgW, self.imgH) = self.image.get_size()

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
        screen.blit(self.image, (self.pos.x, self.pos.y))
        #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT))

class beerStack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = random.randint(1, 4)
        self.stack = []
        for i in range(self.width):
            self.height = random.randint(1, 4)
            for j in range(self.height):
                beer = Obstacles(False)
                beer.pos.y -= 20 * (j)
                beer.pos.x -= 20 * (i)
                self.stack.append(beer)

    def draw(self, screen):
        for beer in self.stack:
            beer.draw()
