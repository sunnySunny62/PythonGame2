import pygame
import os
pygame.init()

win = pygame.display.set_mode((1000,500))

# loading image file inside bg_img variable
bg_img = pygame.image.load("Background.png")

# scale our image according to the window size/surface
bg = pygame.transform.scale(bg_img, (1000, 500))

width = 1000
i = 0

run = True
while run:
    #pygame.time.delay()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    win.blit(bg, (i, 0))
    win.blit(bg, (width + i, 0))
    
    if i == -width:
        win.blit(bg, (width + i, 0))
        i = 0
    i -= 4

    pygame.display.update()