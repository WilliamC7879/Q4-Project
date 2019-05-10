import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,700))

pygame.display.set_caption("tutorial follow along")

radius = 20
x = 250
y = 800 - radius
ySpeed = 20
jumping = False #for sprite
falling = False
vel = 5
#jumplist = 0
points = 0

font = pygame.font.SysFont('comicsans', 30, True)

yWeights = [0] * 800
run = True
print(yWeights)
while run:
    pygame.time.delay(1) #100 miliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #jumplist += 1
                ySpeed = int(ySpeed + 15)#jumplist/2)
                jump = True
                if (y < 700 and y > 660):
                    points += 3
                if (y < 660 and y > 580):
                    points += 2
                if (y < 580 and y > 460):
                    points += 1
                if(y < 460 ):
                    points -= 1
                if (y == 700 - radius):
                    points = 0



    pygame.draw.circle(win, (125, 125, 125), (250, 250), 500)
    pygame.draw.rect(win, (225,0,0), (0,660,500,40))
    pygame.draw.rect(win, (225,225,0),(0,580,500,80))
    pygame.draw.rect(win,(0,225,0), (0,460,500,120))
    pygame.draw.rect(win,(0,0,0), (0,0,500,460))
    pygame.draw.circle(win, (125,0, 250),(x,y),radius)
    text = font.render('POINTS: ' + str(points), 1, (255, 0, 0))

    win.blit(text, (250 - (text.get_width()/2), 200))

    print(y)
    print(str(yWeights[y]) + " COMPARED TO " + str(0 - (random.random() < .3)))
    if(yWeights[y] > 0 - (random.random() < .3)):
        pointsThatWeGotForJump = 0
        ySpeed = int(ySpeed + 15)#jumplist/2)
        jump = True
        if (y < 700 and y > 660):
            pointsThatWeGotForJump += 3
        if (y < 660 and y > 580):
            pointsThatWeGotForJump += 2
        if (y < 580 and y > 460):
            pointsThatWeGotForJump += 1
        if(y < 460 ):
            pointsThatWeGotForJump -= 10
        if (y == 700 - radius):
            pointsThatWeGotForJump = 0

        points += pointsThatWeGotForJump
        yWeights[y] = (yWeights[y] + pointsThatWeGotForJump)/2



    

    y = y - ySpeed
    ySpeed = ySpeed - 1
    pygame.display.update()
    
    # if the y position is off the screen on the bottom
    if (y > 700 - radius):
        ySpeed = 0
        y = 700 - radius

    if (y < 0 + radius):
        ySpeed = 0
        y = 1 + radius

pygame.quit()