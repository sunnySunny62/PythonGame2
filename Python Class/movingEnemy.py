import pygame
import os
pygame.init()

win = pygame.display.set_mode((500,540))
# loading images for the cenemy
standing = pygame.image.load(os.path.join("Assets/Hero", "standing.png"))

left = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L8E.png"))]


right = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R8E.png"))]
#properties for enemy
x = 250
y = 250
vel = 10

# varibales for moving the animations
move_left = False
move_right = False
step_Index = 0

def draw_enemy():
    global step_Index
    win.fill((0, 0, 0)) # draw canvas
    if step_Index >= 32:
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

    draw_enemy()

    userInput = pygame.key.get_pressed() # variable for movement
    if userInput[pygame.K_LEFT] and x > 0: # left x = 0 <-- will change with canvas size
        x -= vel
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT] and x < 440: # Right x = 500 <-- will change with canvas size
        x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        step_Index = 0

    pygame.time.delay(30)
    pygame.display.update()