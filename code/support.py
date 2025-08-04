from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path, "r") as level_map:
        layout = reader(level_map, delimiter = ",")
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map

def import_folder(path):
    surface_list = []

    for _,__, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def import_folder_with_names(path):
    surface_dict = {}
    print('importing a folder')
    for _,__, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_dict[image.split(".")[0]] = image_surf

    return surface_dict

def import_folder_subfolder_with_names(path):
    """returns a dict [subfolder_names]: dict( [file_name]:imported_image )"""
    subfolder_dict = {}

    for _, folders, __ in walk(path):
        for folder in folders:
            full_path = path + '/' + folder
            subfolder_dict[folder] = import_folder_with_names(full_path)

    return subfolder_dict

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    print(import_folder_subfolder_with_names('../graphics/weapons'))