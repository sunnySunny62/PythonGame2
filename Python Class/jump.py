import pygame

pygame.init()

win = pygame.display.set_mode((500,540))


#properties for character
x = 250
y = 400
radius = 20
vel_x = 10
vel_y = 10
jump = False

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
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500: # Right x = 500 <-- will change with canvas size
        x += vel_x

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


    win.fill((33, 75, 148)) #fill window with color so the window gets updated
    pygame.draw.circle(win,(232, 226, 176),(int(x), int(y)) ,radius)
    pygame.display.update()

pygame.quit()