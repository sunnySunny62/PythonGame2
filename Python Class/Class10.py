import pygame
import os
import random

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

#importing enemy images
Eleft = [pygame.image.load(os.path.join("Assets/Enemy", "L1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L8E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L9P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L10P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "L11P.png"))]

Eright = [pygame.image.load(os.path.join("Assets/Enemy", "R1E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R2E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R3E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R4E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R5E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R6E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R7E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R8E.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R9P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R10P.png")),
        pygame.image.load(os.path.join("Assets/Enemy", "R11P.png"))]

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

class Enemy():
    def __init__(self, x, y, direction):
        self.x =  x
        self.y = y
        self.direction = direction
        self.step_index = 0

    def step(self):
        if self.step_index >= 33: #using 33 instead of 11 because runs smoother and without glitch
            self.step_index = 0
    
    def draw_enemy(self, win):
        self.step()
        if self.direction == left:
            win.blit(Eleft[self.step_index//3],(self.x,self.y))
        if self.direction == right:
            win.blit(Eright[self.step_index//3],(self.x,self.y))
        self.step_index += 1

    def move_enemy(self):
        if self.direction == left:
            self.x -= 3
        if self.direction == right:
            self.x += 3

    def off_screen(self):
        return not(self.x >= -50 and self.x <= win_width + 50)

# main funciton
def game():
    win.fill((0, 0, 0))
    win.blit(bg, (0, 0))
    player.draw_character(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    for enemy in enemies:
        enemy.draw_enemy(win)
    pygame.time.delay(30)
    pygame.display.update()


# Instance of Hero-Class
player = Hero(250, 300)

#Instance of Enemy-Class
enemies = []

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

    # call all functions of enemy
    if len(enemies) == 0:
        rand_n = random.randint(0,1)
        if rand_n == 1:
            enemy = Enemy(750, 300, left)
            enemies.append(enemy)
        if rand_n == 0:
            enemy = Enemy(50, 300, right)
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move_enemy()
        if enemy.off_screen():
            enemies.remove(enemy)
    game()