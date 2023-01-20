import pygame
from pygame import event

pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("REGGIN<3")
screen.fill([0, 0, 0])

#joonistamine
pygame.draw.rect(screen, [255, 255, 255], [100, 20, 100, 240], 1)
pygame.draw.rect(screen, [255, 255, 255], [145, 259, 10, 32], 1)
pygame.draw.circle(screen, [0, 255, 0], [150,70], 30, 0)
pygame.draw.circle(screen, [255, 255, 0], [150,140], 30, 0)
pygame.draw.circle(screen, [255, 0, 0], [150,210], 30, 0)
pygame.draw.polygon(screen, [0, 0, 255], [[170,290],[180,300],[170,290],[130,290],[120,300],[180,300]], 0)
pygame.display.flip()

running = True

# Loop
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False