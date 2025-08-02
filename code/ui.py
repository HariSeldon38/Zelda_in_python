import pygame
from settings import *

class UI:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #bar setup
        self.health_bar_rect = pygame.Rect(10,10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10,34, ENERGY_BAR_WIDTH,BAR_HEIGHT)

        #convert weapon dict
        self.weapon_graphics = [] #list of loaded full.png weapon
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        #convert magic dict
        self.magic_graphics = []
        for magic in magic_data.values():
            path = magic['graphic']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)

    def show_bar(self, current_amount, max_amount, bg_rect, color):
        #draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        #convert stat to px
        ratio = current_amount / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        #drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_xp(self, xp):
        text_surf = self.font.render(str(int(xp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright= (x,y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20,20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    def show_selection_box(self, left, bottom, has_switched=False):
        bg_rect = pygame.Rect(0, 0, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        bg_rect.bottomleft = (left,bottom)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BG_COLOR_ACTIVE, bg_rect)
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def show_weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.show_selection_box(87, 710, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)

    def show_magic_overlay(self, magic_index, has_switched):
        bg_rect = self.show_selection_box(17, 700, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)

        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        self.show_xp(player.xp)

        self.show_selection_box(157, 700) # = empty overlay for now
        self.show_magic_overlay(player.magic_index, not player.can_switch_magic)
        self.show_weapon_overlay(player.weapon_index, not player.can_switch_weapon)


