import pygame
from support import import_folder_with_names

class Weapon(pygame.sprite.Sprite):

    all_weapons_images = {} #store images after they have been loaded (ie when first using a weapon)

    def __init__(self, player,groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        self.player = player
        if player.weapon not in Weapon.all_weapons_images:
            path  = f'../graphics/weapons/{player.weapon}'
            Weapon.all_weapons_images[player.weapon] = import_folder_with_names(path)

        self.images = self.all_weapons_images[player.weapon]
        self.direction = player.status.split("_")[0]
        self.image = self.images[self.direction]
        #placement
        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
        elif self.direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0,16))
        elif self.direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-10,0))
        elif self.direction == 'up':
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(-12,0))

    def update_position(self):
        if self.direction == 'right':
            self.rect = self.image.get_rect(midleft=self.player.rect.midright + pygame.math.Vector2(0, 16))
        elif self.direction == 'left':
            self.rect = self.image.get_rect(midright=self.player.rect.midleft + pygame.math.Vector2(0, 16))
        elif self.direction == 'down':
            self.rect = self.image.get_rect(midtop=self.player.rect.midbottom + pygame.math.Vector2(-10, 0))
        elif self.direction == 'up':
            self.rect = self.image.get_rect(midbottom=self.player.rect.midtop + pygame.math.Vector2(-12, 0))

    def update(self):
        new_direction = self.player.status.split("_")[0]
        if new_direction != self.direction:
            self.direction = new_direction
            self.image = self.images[self.direction]
        self.update_position()


