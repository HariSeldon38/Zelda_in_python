import pygame
from settings import *
from player import Player
from tile import Tile
from debug import debug

class Level:
    def __init__(self):

        # get display surf from anywhere in the code
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, square in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if square == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                if square =='p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YsortCameraGroup(pygame.sprite.Group):
    """This sprite group is going to fonction as a camera
    and we are going to sort the sprites by Y coordinate and give them some overlap
    ie we want sprites with lower Y value (upper) to be displayed first
    and then the rows bellow will overlap the previous ones"""

    def __init__(self):
        super().__init__()

        #general setup
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        #getting the offset
        self.offset.x = -player.rect.centerx + self.half_width # we want player.rect.centerx displayed in pos self.half_width
        self.offset.y = -player.rect.centery + self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offseted_position = sprite.rect.topleft + self.offset #tuple

            self.display_surface.blit(sprite.image, offseted_position)