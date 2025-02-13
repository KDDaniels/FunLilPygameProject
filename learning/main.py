#!/usr/bin/env python

import pygame
from other import OtherFile
from potato import Potato

def main():
    other = OtherFile()
    other.test("hello from OtherFile!")

    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    # Initializes a Potato object and adds it to the sprite list
    p = Potato(50, 50)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(p)

    running = True
    clock = pygame.time.Clock()
    delta_time = 0.1


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # calles update() on all of the sprites in the group and then draws them
        all_sprites.update()
        all_sprites.draw(screen)

        # updates the display
        pygame.display.flip()
        
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
    
    pygame.quit()


if __name__ == "__main__":
    main()