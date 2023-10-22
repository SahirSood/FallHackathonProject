import pygame
import random
import os
class Level:
    def __init__(self, tile_width, tile_height, screen_width, screen_height):
        pygame.init()
        self.PlainTile = pygame.image.load(os.path.join('TileSet', '1 Tiles', 'Tile_11.png'))
        self.TopTile = pygame.image.load(os.path.join('TileSet', '1 Tiles', 'Tile_03.png'))
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_grid = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scroll_x = 0  # Keep track of horizontal scrolling
        self.scroll_speed = 2  # Adjust the scrolling speed
        self.level_width = len(self.tile_grid[0]) * tile_width

    def load_level(self, screen):
        for row_index, row in enumerate(self.tile_grid):
            for col_index, tile_type in enumerate(row):
                # Draw a tile at this position
                tile_x = col_index * self.tile_width - self.scroll_x
                tile_y = row_index * self.tile_height
                if tile_type == 1:
                    screen.blit(self.PlainTile, (tile_x, tile_y))
                elif tile_type == 2:
                    screen.blit(self.TopTile, (tile_x, tile_y))
        
    def scroll(self):
        self.scroll_x = (self.scroll_x + self.scroll_speed) % self.level_width

        