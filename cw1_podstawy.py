import pygame
from sys import exit
pygame.init()  # zainicjalizowanie silnika pygame

X, Y = 400, 200
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

    # screen.blit(test_surface, (0, 0))


    pygame.draw.rect(screen, "White", (X, Y, 10, 10))
    # pygame.draw.line(screen, (128, 128, 128), (10, 200), (10, 300), 5)

    # wypisywanie tekstu
    # font = pygame.font.SysFont("Arial", 24)
    # label = font.render("Hello World", 1, 'White')
    # screen.blit(label, (10, 10))

    step = 5
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        X -= step
    if keys[pygame.K_RIGHT]:
        X += step
    if keys[pygame.K_UP]:
        Y -= step
    if keys[pygame.K_DOWN]:
        Y += step

    screen.fill("Black")
    pygame.draw.rect(screen, "White", (X, Y, 10, 10))

    pygame.display.update()
    clock.tick(60)  #framerate (60fps)

