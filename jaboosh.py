import pygame
import random
import sklearn
from sklearn.neural_network import MLPClassifier

# INIT
pygame.init()
win = pygame.display.set_mode((500,700))
pygame.display.set_caption("REWARD JUMP")

# VARIABLES
radius = 20
y = 800 - radius
ySpeed = 20
points = 0
font = pygame.font.SysFont('comicsans', 30, True)
train = True
run = True

def jump():
    global ySpeed
    ySpeed += int(ySpeed + 30)
    
    pointsGained = 0
    if (y < 700 and y > 660):
        pointsGained += 3
    if (y < 660 and y > 580):
        pointsGained += 2
    if (y < 580 and y > 460):
        pointsGained += 1
    if(y < 460 ):
        pointsGained -= 1
    if (y == 700 - radius):
        pointsGained = 0
    
    return pointsGained

def ensureBallIsWithinScreen():
    global y
    global ySpeed

    if (y > 700 - radius):
        ySpeed = 0
        y = 700 - radius

    if (y < 0 + radius):
        ySpeed = 0
        y = 1 + radius
    return

def mainGameLoopUpdate():
    global y 
    global ySpeed

    ySpeed -= 1
    y -= ySpeed
    
    pygame.display.update()

    ensureBallIsWithinScreen()
    return

def mainPygameDisplayLoopUpdate():
    global run 
    global points
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                points += jump()
                
    pygame.draw.circle(win, (125, 125, 125), (250, 250), 500)
    pygame.draw.rect(win, (225,0,0), (0,660,500,40))
    pygame.draw.rect(win, (225,225,0),(0,580,500,80))
    pygame.draw.rect(win,(0,225,0), (0,460,500,120))
    pygame.draw.rect(win,(0,0,0), (0,0,500,460))
    pygame.draw.circle(win, (125,0, 250),(250,y),radius)
    text = font.render('POINTS: ' + str(points), 1, (255, 0, 0))
    win.blit(text, (250 - (text.get_width()/2), 200))
    return

while run:
    pygame.time.delay(25) #miliseconds
    mainGameLoopUpdate()
    mainPygameDisplayLoopUpdate()

pygame.quit()
