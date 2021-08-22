import pygame
import os

pygame.init()

win = pygame.display.set_mode((500,540))

# loading images for the character
standing = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))

left = [pygame.image.load(os.path.join("Assets/Hero", "L1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "L9.png"))]

right = [pygame.image.load(os.path.join("Assets/Hero", "R1.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R2.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R3.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R4.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R5.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R6.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R7.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R8.png")),
        pygame.image.load(os.path.join("Assets/Hero", "R9.png"))]

#properties for character
x = 250
y = 250
vel = 10

# varibales for moving the animation left and right
move_left = False
move_right = False
step_Index = 0

def draw_character():
    global step_Index
    win.fill((0, 0, 0)) # draw canvas
    if step_Index >= 36:
        step_Index = 0
    if move_left: # loop helps to show the image in the canvas (Adding the "left" variable)
        win.blit(left[step_Index // 4], (x, y))
        step_Index += 1
    elif move_right:
        win.blit(right[step_Index // 4], (x, y))
        step_Index += 1
    else:
        win.blit(standing, (x, y))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_character()

    userInput = pygame.key.get_pressed() # variable for movement
    if userInput[pygame.K_LEFT] and x > 0: # left x = 0 <-- will change with canvas size
        x -= vel
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT] and x < 500: # Right x = 500 <-- will change with canvas size
        x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        step_Index = 0

    pygame.time.delay(30)
    pygame.display.update()