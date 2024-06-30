import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nieskończony bieg")
clock = pygame.time.Clock()

background_surface = pygame.image.load('images_PG/background.png').convert()
mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(topleft=(500, 300))
# mushroom_pos_x = 500

player_surface = pygame.image.load('images_PG/girl_stay.png')
player_rect = player_surface.get_rect(midbottom=(60, 360))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("Zderzenie")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("Nacisnieto klawisz myszy")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom == 360:
                #print("Skok - spacja")
                player_gravity = -20

    screen.blit(background_surface, (0, 0))

    step = 5
    # mushroom_pos_x -= step
    # if mushroom_pos_x < -100:
    #     mushroom_pos_x = 700
    mushroom_rect.x -= step
    if mushroom_rect.right < 0:
        mushroom_rect.left = 700
    #screen.blit(mushroom_surface, (mushroom_pos_x, 300))
    screen.blit(mushroom_surface, mushroom_rect)

    # if player_rect.colliderect(mushroom_rect):
    #     print("Doszło do zderzenia")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("Zderzenie z myszą")
    #     print(pygame.mouse.get_pressed())

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 360:
        player_rect.bottom = 360
    screen.blit(player_surface, player_rect)


    # skakanie
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("Nacisnieto spacje")

    pygame.display.update()
    clock.tick(60)  # framerate (60fps)

