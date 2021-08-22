import pygame
import os

pygame.init()
win_height = 400
win_width = 800

#window fill and dimensions
win = pygame.display.set_mode((win_width, win_height))

#enemy animations
left = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L8E.png"))]

right = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R8E.png"))]

#bullet image
bullet_img = pygame.image.load(os.path.join("Assets/Bullets", "light_bullet.png"))
bi = pygame.transform.scale(bullet_img, (15, 15))

#Background image
bg_img = pygame.image.load("Background.png")
bg = pygame.transform.scale(bg_img, (win_width, win_height))

class Enemy:
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

    #draw enemy
    def draw_enemy(self, win):
        if self.stepIndex >= 8:
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

    def shoot_bullet(self):
        if userInput[pygame.K_SPACE]:
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
        for bullet in self.bullets:
            bullet.move_bullet()

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

# main funciton
def game():
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    player.draw_enemy(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    pygame.time.delay(30)
    pygame.display.update()

player = Enemy(250, 300)

#main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    #calling all functions
    player.movement(userInput)
    player.Jump(userInput)
    player.shoot_bullet()
    game()