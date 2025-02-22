#!/usr/bin/env python

import pygame
from src.wizard import Wizard
from src.data import rects

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    bg = pygame.image.load("resources/images/backgrounds/Background.jpg").convert()
    

    pc = Wizard("Hat", 0,0, 5, 100)
    sprites = pygame.sprite.Group(pc)

    rect_color = (200, 100, 100)
    rect_pos = [400, 200, 100, 300]

    wall = pygame.Rect(rect_pos)
    wall2 = pygame.Rect(200, 400, 300, 100)
    rects.append(wall)
    rects.append(wall2)

    clock = pygame.time.Clock()
    delta_time = 0.1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        screen.blit(bg, (0,0))

        pygame.draw.rect(screen, rect_color, wall)
        pygame.draw.rect(screen, rect_color, wall2)
        
        sprites.update()
        sprites.draw(screen)

        pygame.display.flip()

        delta_time = clock.tick(FPS) / 1000
        delta_time = max(0.001, min(0.1, delta_time))

    pygame.quit()

if __name__ == "__main__":
    main()