import pygame
import json

class Character(pygame.sprite.Sprite):
    def __init__(self, char, x=0, y=0):
        super().__init__()
        self.load_data("resources/data/characters/characters.json", char)

    def load_data(self, path, char):
        # load data from json path
        with open(path) as f:
            j = json.load(f)

            print(j[char])
            

