import pygame
import os
import math
from pygame.locals import *
import player
pygame.init()

#Setting up frames and clock varaibles
clock = pygame.time.Clock()
FPS = 60


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
pygame.draw.rect(screen, colour, pygame.Rect(30, 30, 30, 30))

#load Image
bg = pygame.image.load(os.path.join('Background Images', 'city 4', '9.png'))
bg = pygame.transform.scale(bg, (SCREEN_HEIGHT,SCREEN_WIDTH))
bg_width = bg.get_width()


#define game variables
scroll = 0
titles =  math.ceil(SCREEN_WIDTH / bg_width) + 1

#Font Settings
myfont = pygame.font.SysFont("Comic Sans", 24)  # Increase font size for better visibility
score_font = pygame.font.SysFont("Comic Sans", 24)
randNumLabel = myfont.render("Score:", 1, (0, 0, 0))


run = True
while run:

    clock.tick(FPS)
    #draw scolling background
    for i in range(0,titles):
        screen.blit(bg,(i*bg_width + scroll,0))

    #scroll background
    scroll -=2

    #reset Scroll
    if abs(scroll) > bg_width: 
        scroll = 0



    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    p1.move()

    #Updating score on screen
    score_text = score_font.render(f"Score: {p1.SCORE}", True, (255, 255, 255))  # You can change the color
    screen.blit(score_text, (10, 10))  # Adjust the position as needed

    # Drawing player
    pygame.draw.rect(screen, colour, pygame.Rect(p1.pos[0], p1.pos[1], p1.WIDTH, p1.HEIGHT))
    
    # Update Display
    
    # After each tick increment score
    pygame.display.update()
    FramePerSec.tick(FPS)
    frameCount += 1
    if frameCount == 5:
        p1.incrementScore()
        frameCount = 0

pygame.quit()



