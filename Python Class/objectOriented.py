import pygame
import os

pygame.init()
win_height = 400
win_width = 800
#window fill and dimensions
win = pygame.display.set_mode((win_width, win_height))

#character animations
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

#bullet image
bullet_img = pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png"))
bi = pygame.transform.scale(bullet_img, (15, 15))

#Background image
bg_img = pygame.image.load("Background.png")
bg = pygame.transform.scale(bg_img, (win_width, win_height))

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False
        self.bullets = []
        self.cool_down_count = 0

    #movement function
    def movement(self, userInput):
        if (userInput[pygame.K_RIGHT]) and self.x <= win_width - 60:
            self.x += self.vel_x
            self.face_right = True
            self.face_left = False
        elif (userInput[pygame.K_LEFT]) and self.x >= 0:
            self.x -= self.vel_x
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    #draw characters
    def draw_character(self, win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    #jumping
    def Jump(self, userInput):
        if userInput[pygame.K_UP] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vel_y * 4
            self.vel_y -= 1
        if self.vel_y < -10:
            self.jump = False
            self.vel_y = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def Cool_Down(self):
        if self.cool_down_count >= 7:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot_bullet(self):
        self.Cool_Down()
        if (userInput[pygame.K_SPACE] and self.cool_down_count == 0):
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
            self.cool_down_count = 1
        for bullet in self.bullets:
            bullet.move_bullet()
            # removes the bullet when they are off the screen
            if bullet.off_screen():
                self.bullets.remove(bullet)

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x + 15
        self.y = y + 25
        self.direction = direction

    def draw_bullet(self):
        win.blit(bi, (self.x,  self.y))

    def move_bullet(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

# check if the bullet is of off the sceen or not (fixes the memory leak issue)
    def off_screen(self):
        return not(self.x >= 0 and self.x <= win_width)


# main funciton
def game():
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    player.draw_character(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    pygame.time.delay(30)
    pygame.display.update()

player = Hero(250, 300)

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #name spacing
    userInput = pygame.key.get_pressed()

    #calling all our functions
    player.movement(userInput)
    player.Jump(userInput)
    player.shoot_bullet()
    game()