import pygame
import os
import math
from pygame.locals import *
import button
import player

# setting up frames and clock varaibles
clock = pygame.time.Clock()
FPS = 60

pygame.init()

# setting screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)
vec = pygame.math.Vector2
frameCount = 0

# creating screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((192, 192, 192)) 

# game variables
game_paused = False

# define fonts and font colour
font = pygame.font.SysFont("lucidaconsole", 40)
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# initializing player character
colour = (0, 128, 0)

FramePerSec = pygame.time.Clock()

# coordinates for player
x = 100
y = 50
p1 = player.Player()

# load button images 
resume_image = pygame.image.load('resume.png').convert_alpha()
quit_image = pygame.image.load('quit.png').convert_alpha()

# create button instances
resume_button = button.Button(304, 65, resume_image, 1)
quit_button = button.Button(336, 185, quit_image, 1)

# loading background
bg = pygame.image.load(os.path.join('Background Images', 'city 4', '9.png'))
bg = pygame.transform.scale(bg, (SCREEN_HEIGHT,SCREEN_WIDTH))
bg_width = bg.get_width()

# define game variables
scroll = 0
titles =  math.ceil(SCREEN_WIDTH / bg_width) + 1

# initializing game loop
run = True
while run:

    clock.tick(FPS)
    #draw scolling background
    for i in range(0,titles):
        screen.blit(bg,(i*bg_width + scroll,0))

    # scroll background
    scroll -=2

    # reset scroll
    if abs(scroll) > bg_width: 
        scroll = 0

    # check if the game is paused 
    if game_paused == True:
        if resume_button.draw(screen):
            game_paused = False
        if quit_button.draw(screen):
            run = False    
        
    # event handler
    for event in pygame.event.get():
        # pausing the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                game_paused = True

        if event.type == pygame.QUIT: 
            print("Game closed.")
            run = False
    
    # player movement
    p1.move()
    pygame.draw.rect(screen, colour, pygame.Rect(p1.pos[0], p1.pos[1], p1.WIDTH, p1.HEIGHT))
    
    pygame.display.update()
    FramePerSec.tick(FPS)
    frameCount += 1
    if frameCount == 5:
        p1.incrementScore()
        frameCount = 0

    pygame.display.update()

pygame.quit()