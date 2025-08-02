import pygame
from settings import *

class Upgrade:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nb = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.max_values = list(player.max_stats.values())

        #selection system
        self.selection_index = 2
        self.selection_time = None
        self.can_move = True

        #overlay dimensions
        self.height = self.display_surface.get_size()[1] * 0.74
        self.width = self.display_surface.get_size()[0] // 6

        self.create_items()

    def create_items(self):
        self.item_list = []

        for index in range(self.attribute_nb):
            #horizontal
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nb
            left = (index * increment) + (increment-self.width) // 2
            #vertical
            top = self.display_surface.get_size()[1] * 0.1
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nb-1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index > 0:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.item_list[self.selection_index].upgrade_stats(self.player)


    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 250:
                self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()
        for index, item in enumerate(self.item_list):

            #get attribute
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface, self.selection_index, name, value, max, cost)


class Item:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0,20))

        cost_surf = self.font.render(str(int(cost)), False, color)
        cost_rect = cost_surf.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0,20))

        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)

    def display_bar(self, surface, value, max, selected):
        top = self.rect.midtop + pygame.math.Vector2(0,60)
        bottom = self.rect.midbottom + pygame.math.Vector2(0,-60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        #cursor setup
        full_height = bottom[1]-top[1]
        relative_number = (value/max)*full_height
        value_rect = pygame.Rect(top[0] - 15, bottom[1] - relative_number, 30, 10)

        pygame.draw.line(surface, color, top, bottom, 5)
        pygame.draw.rect(surface, color, value_rect)

    def upgrade_stats(self, player):
        up_stat = list(player.stats.keys())[self.index]
        if player.xp >= player.upgrade_cost[up_stat] and player.stats[up_stat] < player.max_stats[up_stat]:
            player.xp -= player.upgrade_cost[up_stat]
            player.stats[up_stat] += 1
            player.upgrade_cost[up_stat] *= 1.4


    def display(self, surface, selected_index, name, value, max, cost):
        if self.index == selected_index:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        self.display_names(surface, name, cost, self.index == selected_index)
        self.display_bar(surface, value, max, self.index == selected_index)