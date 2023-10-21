import pygame
from pygame.locals import *
import player
pygame.init()

# Setting screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)
vec = pygame.math.Vector2
FPS = 60
frameCount = 0

# Creating a screen with a grey background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((192, 192, 192))  # Color should be a tuple

# Initializing color
colour = (0, 128, 0)

FramePerSec = pygame.time.Clock()

# Coordinates for player
x = 100
y = 50
p1 = player.Player()

# Drawing a rectangle
pygame.draw.rect(screen, colour, pygame.Rect(30, 30, 60, 60))



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                p1.jump()
    p1.move()
    pygame.draw.rect(screen, colour, pygame.Rect(p1.pos[0], p1.pos[1], p1.WIDTH, p1.HEIGHT))
    
    pygame.display.update()
    FramePerSec.tick(FPS)
    frameCount += 1
    if frameCount == 60:
        p1.incrementScore()
        frameCount = 0
    screen.fill((0, 0, 0)) #clear screen

pygame.quit()



