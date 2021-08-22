import pygame
import os
pygame.init()

win = pygame.display.set_mode((1000,500))
# loading image file inside the variable
bg_img = pygame.image.load("background.jpg")
# scale the image according to the window size
bg = pygame.transform.scale(bg_img, (1000, 500))

width = 1000
i = 0

run = True
while run:
    pygame.time.delay(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))

    win.blit(bg, (i, 0))
    win.blit(bg, (width + i, 0))
    
    if i == -width:
        win.blit(bg, (width + i, 0))
        i = 0
    i -= 1

    pygame.display.update()
#pygame.quit()