import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

punaneposx = 290

sinine_auto = pygame.image.load("img/f1_blue.png")
sinine_auto = pygame.transform.scale(sinine_auto, [60, 150])
sinine_posx, sinine_posy = 170, -210

sinine_auto2 = pygame.image.load("img/f1_blue.png")
sinine_auto2 = pygame.transform.scale(sinine_auto2, [60, 150])
sinine_posx2, sinine_posy2 = 420, -300

kiirus = 3
score_font = pygame.font.SysFont("times New Roman", 30)


def skoor(score):
    value = score_font.render("Sinu skoor: " + str(score), True, [0, 0, 0])
    screen.blit(value, [0, 0])


def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)


lopp_skoor = 0
mang_labi = False
while not mang_labi:
    clock.tick(60)
    # mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
