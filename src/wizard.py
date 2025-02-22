import pygame
from .character import Character
from src.data import rects

class Wizard(Character):
    def __init__(self, char, x=0, y=0, movement_speed=5, movement_step=20):
        super().__init__(char=char)
        self.image = pygame.image.load("resources/images/characters/Hat.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.angle = 0
        self.old_angle = self.angle

        self.movement_speed = movement_speed
        self.movement_step = movement_step

        self.target_x = self.rect.x
        self.target_y = self.rect.y

        self.old_target_x = self.target_x
        self.old_target_y = self.target_y

    def check_for_collisions(self):
        for obj in rects:
            if self.rect.colliderect(obj):
                return True
        return False
            

    def update(self):
        # checking keys pressed
        keys = pygame.key.get_pressed()
        if self.target_x == self.rect.x and self.target_y == self.rect.y:
            self.old_target_x = self.target_x
            self.old_target_y = self.target_y
            if keys[pygame.K_LEFT]:
                self.target_x = self.rect.x - self.movement_step
                self.angle = 270

            elif keys[pygame.K_RIGHT]:
                self.target_x = self.rect.x + self.movement_step
                self.angle = 90

            elif keys[pygame.K_UP]:
                self.target_y = self.rect.y - self.movement_step
                self.angle = 0

            elif keys[pygame.K_DOWN]:
                self.target_y = self.rect.y + self.movement_step
                self.angle = 180

        
        if self.target_x != self.rect.x or self.target_y != self.rect.y:
            if self.check_for_collisions():
                self.target_x = self.old_target_x
                self.target_y = self.old_target_y

        
        

        

        # lerping
        if self.rect.x < self.target_x:
            self.rect.x += min(self.movement_speed, self.target_x - self.rect.x)
        elif self.rect.x > self.target_x:
            self.rect.x -= min(self.movement_speed, self.rect.x - self.target_x)
        elif self.rect.y < self.target_y:
            self.rect.y += min(self.movement_speed, self.target_y - self.rect.y)
        elif self.rect.y > self.target_y:
            self.rect.y -= min(self.movement_speed, self.rect.y - self.target_y)

        # changing angles
        if self.old_angle != self.angle:
            self.image = pygame.transform.rotate(self.image, self.old_angle)
            self.image = pygame.transform.rotate(self.image, -self.angle)
            self.old_angle = self.angle

