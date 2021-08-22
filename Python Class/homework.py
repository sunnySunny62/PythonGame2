import pygame

pygame.init()

win = pygame.display.set_mode((500,540))


#properties for character
x = 250
x2 = 150
x3 = 350
y = 400
y2 = 400
y3 = 400
radius = 20
vel_x = 10
vel_y = 10
jump = False
jump2 = False
jump3 = False

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
    if userInput[pygame.K_LEFT] and x > 0 and x2 > 0 and x3 > 0: # left x = 0 <-- will change with canvas size
        x -= vel_x
        x2 -= vel_x
        x3 -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500 and x2 < 500 and x3 < 500: # Right x = 500 <-- will change with canvas size
        x += vel_x
        x2 += vel_x
        x3 += vel_x

    # Jumping effect
    # checking is jump is False AND if user is clicking the space button
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y * 5
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    
    if jump2 is False and userInput[pygame.K_UP]:
        jump2 = True
    if jump2 is True:
        y2 -= vel_y * 5
        vel_y -= 1
        if vel_y < -10:
            jump2 = False
            vel_y = 10

    if jump3 is False and userInput[pygame.K_w]:
        jump3 = True
    if jump3 is True:
        y3 -= vel_y * 5
        vel_y -= 1
        if vel_y < -10:
            jump3 = False
            vel_y = 10


    win.fill((33, 75, 148)) #fill window with color so the window gets updated
    pygame.draw.circle(win,(250, 100, 0),(int(x), int(y2)) ,radius)
    pygame.draw.circle(win,(250, 0, 0),(int(x2), int(y)) ,radius)
    pygame.draw.circle(win,(250, 150, 100),(int(x3), int(y3)) ,radius)
    pygame.display.update()

pygame.quit()