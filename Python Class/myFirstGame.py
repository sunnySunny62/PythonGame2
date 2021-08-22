import pygame

pygame.init()

win = pygame.display.set_mode((540,540))


#properties for character
x = 250
y = 250
width = 40
height = 40
vel = 10

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # movement
    # -y = up
    # +y = down
    userInput = pygame.key.get_pressed() # variable for movement
    if userInput[pygame.K_LEFT] and x > 0: # left x = 0 <-- will change with canvas size
        x -= vel
    if userInput[pygame.K_RIGHT] and x < 500: # Right x = 500 <-- will change with canvas size
        x += vel
    if userInput[pygame.K_UP] and y > 0: # Up y = 0 <-- will change with canvas size
        y -= vel
    if userInput[pygame.K_DOWN] and y < 500: # Down y = 500 <-- will change with canvas size
        y += vel

    win.fill((33, 75, 148)) #fill window with color so the window gets updated
    pygame.draw.rect(win,(232, 226, 176),(x, y, width, height))
    pygame.display.update()

pygame.quit()