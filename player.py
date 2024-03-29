import pygame
from pygame.locals import *
import os


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

        # Run Sprites
        self.RunSprites = []
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f1.png')))
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f2.png')))
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f3.png')))
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f4.png')))
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f5.png')))
        self.RunSprites.append(pygame.image.load(os.path.join('RUN', 'f6.png')))
        # Setting up player sprite indexes
        self.CurSprite = 0
        self.image = self.RunSprites[self.CurSprite]
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 100)

        # Variables
        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        #(self.WIDTH, self.HEIGHT) = self.image.get_size()


    def move(self):
        self.acc = vec(0,0.5) 
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT] or pressed_keys[pygame.K_a]:
            self.acc.x = -(ACC)
        if pressed_keys[K_RIGHT] or pressed_keys[pygame.K_d]:
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

        
        # self.rect.midbottom = self.pos
    def draw(self, screen):
        self.CurSprite +=0.15
        if self.CurSprite   >= len(self.RunSprites):
            self.CurSprite = 0
        # pygame.draw.rect(screen, pygame.Rect(self.pos[0], self.pos[1], self.WIDTH, self.HEIGHT))
        
        self.image = self.RunSprites[int(self.CurSprite)]
        self.image = pygame.transform.scale(self.image, (100, 100))
        screen.blit(self.image, (self.pos.x - 2 * self.HEIGHT, self.pos.y - 2 * self.HEIGHT))

    def incrementScore(self):
        self.SCORE += 1        

    def jump(self):
        if self.pos.y >= SCREEN_HEIGHT - self.HEIGHT - 5:
            self.vel.y = self.jumpHeight