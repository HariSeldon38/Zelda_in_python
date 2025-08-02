import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        #paths should be placed in magic dict but for now...
        self.sounds = {'heal': pygame.mixer.Sound('../audio/heal.wav'),
                       'flame': pygame.mixer.Sound('../audio/flame.wav'),}
        self.sounds['heal'].set_volume(0.1)
        self.sounds['flame'].set_volume(0.05)

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            if player.health + strength < player.stats['health']:
                player.health += strength
                player.energy -= cost
                self.animation_player.create_particles('aura', player.rect.center, groups)
                self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0,-60), groups)
                self.sounds['heal'].play()
            elif player.health < player.stats['health']:
                player.health = player.stats['health']
                player.energy -= cost
                self.animation_player.create_particles('aura', player.rect.center, groups)
                self.animation_player.create_particles('heal', player.rect.center + pygame.math.Vector2(0,-60), groups)
                self.sounds['heal'].play()

    def flame(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            self.sounds['flame'].play()

            if player.status.split('_')[0]=='right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0]=='left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0]=='up':  direction = pygame.math.Vector2(0,-1)
            elif player.status.split('_')[0]=='down': direction = pygame.math.Vector2(0,1)

            for i in range(1,6):
                if direction.x: #horizontal
                    offset_x = TILESIZE*i*direction.x
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_particles('flame',(x,y), groups, sprite_type='flame')
                elif direction.y: #vertical
                    offset_y = TILESIZE*i*direction.y
                    x = player.rect.centerx + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + offset_y + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_particles('flame',(x,y), groups, sprite_type='flame')