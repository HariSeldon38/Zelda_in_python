import pygame
from random import choice
from settings import *
from support import *
from tile import Tile
from player import Player
from weapon import Weapon
from enemy import Enemy
from ui import UI

class Level:
    def __init__(self):

        #get display surf from anywhere in the code
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        #attack sprites
        self.current_attack = None

        #sprite setup
        self.create_map()

        #user interface
        self.ui = UI()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/antoine_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/antoine_Grass.csv'),
            'object': import_csv_layout('../map/antoine_Objects.csv'),
            'entities': import_csv_layout('../map/antoine_Entities.csv')
        }
        graphics = {
            'grass': import_folder('../graphics/grass'),
            'objects': import_folder('../graphics/objects'),
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, square in enumerate(row):
                    if square != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(square)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                        if style == 'entities':
                            if square == '394':
                                self.player = Player(
                                    (x,y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic,
                                )
                            else:
                                if square == '390': monster_name = 'bamboo'
                                elif square == '390': monster_name = 'spirit'
                                elif square == '392': monster_name = 'raccoon'
                                else: monster_name = 'squid'

                                Enemy(monster_name, (x,y), [self.visible_sprites], self.obstacle_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def create_magic(self, style, strenght, cost):
        print(style)
        print(strenght)
        print(cost)

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill() #kill is a pygame fct that delete a sprite (so it seems)
        self.current_attack = None

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)

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

        #creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground_antoine.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))

    def custom_draw(self, player):

        #getting the offset
        self.offset.x = -player.rect.centerx + self.half_width # we want player.rect.centerx displayed in pos self.half_width
        self.offset.y = -player.rect.centery + self.half_height

        #drawing the floor
        floor_offseted_pos = self.floor_rect.topleft + self.offset
        self.display_surface.blit(self.floor_surf, floor_offseted_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offseted_position = sprite.rect.topleft + self.offset #tuple

            self.display_surface.blit(sprite.image, offseted_position)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)