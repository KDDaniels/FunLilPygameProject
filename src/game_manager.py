import pygame
import json
from .wizard import Wizard

class GameManager:
    """
    Class representing a GameManager object
    """
    def __init__(self,path):
        """
        Initializes a GameManager object

        Parameters
        ----------
        path : string
            path to the settings.json file
        """
        pygame.init()

        self.gamestate = "menu"
        self.current_level = 0
        self.is_loaded = False

        self.delta_time = 0.1
        self.clock = pygame.time.Clock()

        self.load_settings(path)

        self.running = True
        self.main_loop()

    def load_settings(self, path):
        """
        Loads the game settings from the settings.json file

        Parameters
        ----------
        path : string
            path to the settings.json file
        """
        with open(path) as f:
            settings = json.load(f)
            self.screen = pygame.display.set_mode((
                int(settings["screen"]["width"]),
                int(settings["screen"]["height"])
                ))
            self.fps = int(settings["screen"]["fps"])


    def load_level(self, level_name):
        """
        Loads a level from levels.json

        Parameters
        ----------
        level_name : string
            name of the level to load
        """
        print(level_name)
        self.bg = pygame.image.load("resources/images/backgrounds/Background.jpg").convert()

    def load_character(self, char_name):
        """
        Loads a character from characters.json and adds to self.sprites

        Parameters
        ----------
        char_name : string
            name of the character to load
        """
        self.pc = Wizard("Hat", 0,0, 5, 100)
        self.sprites.add(self.pc)

    def main_loop(self):
        """
        Main game loop to run updates
        """
        while self.running:
            self.update()

    def update(self):
        """
        Updates everything that needs updating
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill((0, 0, 0))
        pygame.display.flip()

        match self.gamestate:
            
            case "menu":
                if not self.is_loaded:
                    self.load_level("menu")
                    self.is_loaded = True
                ...

            case "level1":
                if not self.is_loaded:
                    self.load_level("level1")
                    self.is_loaded = True
                ...

            case "level2":
                if not self.is_loaded:
                    self.load_level("level2")
                    self.is_loaded = True
                ...

            # etc

        self.delta_time = self.clock.tick(self.fps) / 1000
        self.delta_time = max(0.001, min(0.1, self.delta_time))

        