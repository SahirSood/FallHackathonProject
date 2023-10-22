import pygame
import random
import os
import math
class Level:
    def __init__(self, tile_width, tile_height, width, height):
        self.PlainTile = pygame.image.load(os.path.join('TileSet', '1 Tiles', 'Tile_11.png'))
        self.TopTile = pygame.image.load(os.path.join('TileSet', '1 Tiles', 'Tile_03.png'))
        if self.PlainTile is None:
            print("Failed to load PlainTile image")
        self.tile_grid = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.screenHeight = height
        self.tile_height = tile_height
        self.tile_width = self.PlainTile.get_width()
        self.scroll = 0
        self.titles = math.ceil(width / tile_width) + 1

    def load_level(self, screen):
        for row_index, row in enumerate(self.tile_grid):
            for col_index, tile_type in enumerate(row):
                # Draw a tile at this position
                tile_x = col_index * self.tile_width - self.scroll
                tile_y = self.screenHeight -row_index * self.tile_height
                if tile_type == 1:
                    screen.blit(self.PlainTile, (tile_x, tile_y))
                elif tile_type == 2:
                    screen.blit(self.TopTile, (tile_x, tile_y))
        
    def update(self, screen):
            for i in range(0,self.titles):
                screen.blit(self.PlainTile,(i*self.tile_width + self.scroll,0))
                self.scroll -=2
            if abs(self.scroll) > self.tile_width:
                self.scroll =0

        