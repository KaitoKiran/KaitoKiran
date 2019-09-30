import pygame
import random
pygame.init()

window = pygame.display.set_mode((720, 720))

pygame.display.set_caption("Test Game")

score = 0

isJump = False
jumpCount = 10

x = 50
y = 50
width = 50
height = 50
vel = 2

xN = random.uniform(0, 670)
yN = random.uniform(0, 670)
widthN = 50
heightN = 50
velY = random.uniform(1, 5)
velX = random.uniform(1, 5)

xM = 450
yM = 450
widthM = 50
heightM = 50
velM = 1

run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if xM == x:
        if yM == y:
            run = False

    keysP = pygame.key.get_pressed()

    xN += velX
    yN += velY

    if(xN >= 670):
        velX *= -1
    if(xN <= 0):
        velX *= -1
    if(yN >= 670):
        velY *= -1
    if(yN <= 0):
        velY *= -1

    if xM > x:
        xM -= velM
    if xM < x:
        xM += velM
    if yM > y:
        yM -= velM
    if yM < y:
        yM += velM


    if keysP[pygame.K_LEFT] and x >= 0:
        x -= vel
    if keysP[pygame.K_RIGHT] and x <= 670:
        x += vel
    if keysP[pygame.K_UP] and y >= 0:
        y -= vel
    if keysP[pygame.K_DOWN] and y <= 670:
        y += vel


    score += 1

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(window, (0, 0, 255), (xM, yM, widthM, heightM))
    pygame.draw.rect(window, (0, 255, 0), (xN, yN, widthN, heightN))
    pygame.display.update()

score /= 100
print("You got", score, "POINTS!!")