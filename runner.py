import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nieskończony bieg")
clock = pygame.time.Clock()
game_active = True

background_surface = pygame.image.load('images_PG/background.png').convert()

mushroom_surface = pygame.image.load('images_PG/mashroom.png').convert_alpha()
mushroom_rect = mushroom_surface.get_rect(topleft=(500, 300))

player_surface = pygame.image.load('images_PG/girl_stay.png')
player_rect = player_surface.get_rect(midbottom=(60, 360))
player_gravity = 0

font = pygame.font.SysFont("Arial", 24)
game_msg = font.render("Naciśniej spację, żeby zagrać jeszcze raz", 1, "White")
game_msg_rect = game_msg.get_rect(center=(300, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 360:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                mushroom_rect.left = 700

    if game_active:
        screen.blit(background_surface, (0, 0))

        step = 5
        mushroom_rect.x -= step
        if mushroom_rect.right < 0:
            mushroom_rect.left = 700
        screen.blit(mushroom_surface, mushroom_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 360:
            player_rect.bottom = 360
        screen.blit(player_surface, player_rect)

        if player_rect.colliderect(mushroom_rect):
            game_active = False

    else:
        screen.fill("Black")
        screen.blit(game_msg, game_msg_rect)


    pygame.display.update()
    clock.tick(60)  # framerate (60fps)

