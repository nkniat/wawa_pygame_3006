import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nieskończony bieg")
clock = pygame.time.Clock()

background_surface = pygame.image.load('images_PG/background.png').convert()
mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_pos_x = 500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))

    step = 5
    mushroom_pos_x -= step
    if mushroom_pos_x < -100:
        mushroom_pos_x = 700
    screen.blit(mushroom_surface, (mushroom_pos_x, 300))

    pygame.display.update()
    clock.tick(60)  # framerate (60fps)

