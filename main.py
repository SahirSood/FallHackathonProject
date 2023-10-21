import pygame
pygame.init()

# Setting screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.5)

# Creating a screen with a grey background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((192, 192, 192))  # Color should be a tuple

# Initializing color
colour = (0, 128, 0)

# Coordinates for player
x = 100
y = 50

# Drawing a rectangle
pygame.draw.rect(screen, colour, pygame.Rect(30, 30, 60, 60))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    pygame.display.update()

pygame.quit()
