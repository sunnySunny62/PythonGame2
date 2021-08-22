import pygame

pygame.init()

win = pygame.display.set_mode((600,600))


#properties for characters
width = 40
height = 40
vel = 10

#square 1
x = 0
y = 0

#square 2
x2 = 500
y2 = 0

#square 3
x3 = 0
y3 = 500

#square 4
x4 = 500
y4 = 500


run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #loop to make squares stop
    if x < 250 and y < 250:
        #square 1
        x += vel
        y += vel

        #sqaure 2
        x2 -= vel
        y2 += vel

        #square 3
        x3 += vel
        y3 -= vel

        #square 4
        x4 -= vel
        y4 -= vel

    win.fill((0, 0, 0)) #fill window with color so the window gets updated
    pygame.draw.rect(win,(232, 226, 176),(x, y, width, height))
    pygame.draw.rect(win,(0, 0, 255),(x2, y2, width, height))
    pygame.draw.rect(win,(0, 255, 0),(x3, y3, width, height))
    pygame.draw.rect(win,(255, 0, 0),(x4, y4, width, height))
    pygame.display.update()

pygame.quit()