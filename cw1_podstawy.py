import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja pierwsza gra")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 100))
test_surface.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #screen.blit(test_surface, (0, 0))

    pygame.draw.rect(screen, "White", (0, 50, 100, 100))
    pygame.draw.line(screen, (128, 128, 128), (10, 200), (10, 300), 5)

    pygame.display.update()
    clock.tick(60)  #framerate (60fps)

