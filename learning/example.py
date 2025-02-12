# shoutout DaFluffyPotato

import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

potato_img = pygame.image.load("potato.png").convert_alpha()

potato_img = pygame.transform.scale(potato_img,
                                    (potato_img.get_width() / 2,
                                     potato_img.get_height() / 2))

running = True
x = 0
clock = pygame.time.Clock()

delta_time = 0.1


while running:
    screen.fill((255, 255, 255))

    screen.blit(potato_img, (x, 30))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))


pygame.quit()