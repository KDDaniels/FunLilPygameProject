import pygame

class Potato(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("thisguy.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dir = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.dir == 0:
                self.image = pygame.transform.flip(self.image, True, False)
            self.dir = 1
            print("left")

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.dir == 1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.dir = 0
            print("right")

        if keys[pygame.K_UP]:
            self.rect.y -= 5
            print("up")

        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            print("down")


