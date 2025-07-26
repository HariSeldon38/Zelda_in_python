import pygame
from settings import *
from player import Player
from tile import Tile

class Level:
    def __init__(self):

        # get display surf from anywhere in the code
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, square in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if square == 'x':
                    Tile((x,y),[self.visible_sprites])

    def run(self):
        # update and draw the game
        pass