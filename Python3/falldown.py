import pygame
import sys
from pygame.locals import *
import os
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

position = [400, 50]
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


FPS = 100
fpsClock = pygame.time.Clock()
soundCount3 = 0
global soundCount4
soundCount4 = 0


hitsound = pygame.mixer.Sound('hit2.wav')

hitdetect = {}

width = 700
height = 600

CANVAS = pygame.display.set_mode((width, height))
#CANVAS = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

pygame.display.set_caption('FallDown')

#colors
ORANGE = (247, 173, 69)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (223, 250, 47)
GREEN = (46, 242, 53)
PURPLE = (130, 40, 100)
default = WHITE

score = 0
fontObj = pygame.font.SysFont("monospace", 20)
endFont = pygame.font.SysFont("arial", 100)
scoreFont = pygame.font.SysFont("arial", 70)
tedfont = pygame.font.SysFont("arial", 50)


ballx = 250
bally = 50
rad = 20

frameCount = 0
soundCount = 0
soundCount2 = 0


#Collision detection function
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):

    if y2 + w2 >= y1 and y2 - w2 <= y1 + h1 and x2 - w2 <= x1 + w1 and x2 + w2 >= x1:
        global soundCount2

        return True


    else:

        return False



#Rectangle class
class Rect:

    def __init__(self, rectx, recty, rectw, recth):

        self.rectx = rectx

        self.recty = recty

        self.rectw = rectw

        self.recth = recth

    def render(self):

        pygame.draw.rect(CANVAS, WHITE, (self.rectx, self.recty, self.rectw, self.recth))

class Circ:

    def __init__(self, color, circx, speed, circy):

        self.circy = circy
        self.circx = circx
        self.color = color
        self.speed = speed


    def make(self):

        pygame.draw.circle(CANVAS, self.color, (self.circx, self.circy), 20, 0)



speed = 1
level = 100
recty = height + 10
rectx = 100
recth = 10
rectw = 300
mx = 0
my = 0
doll = 1

walls = []
balls = 0
ballist = []
taco = 0
def mainMenu():

    CANVAS.fill(BLACK)
    fallDown = endFont.render("Fall Down", True, WHITE)
    position5Font = fallDown.get_rect()
    position5Font.center = (width - width/2, 200)
    CANVAS.blit(fallDown, position5Font)
    play = tedfont.render("Press Enter to Play", True, WHITE)
    position3Font = play.get_rect()
    position3Font.center = (width/2, 400)
    CANVAS.blit(play, position3Font)
    key = pygame.key.get_pressed()
    global balls

    while balls < 15:
        balls += 1
        global taco
        taco = random.randint(0, 7)
        if taco == 1: culur = WHITE
        elif taco == 2: culur = BLUE
        elif taco == 3: culur = GREEN
        elif taco == 4: culur = PURPLE
        elif taco == 5: culur = YELLOW
        elif taco == 6: culur = ORANGE
        elif taco == 7: culur = ORANGE
        else: culur = PURPLE

        ballist.append(Circ(culur, random.randint(0, width), random.randint(5, 10), -random.randint(30, 100)))
    global height
    for i in ballist:
        i.make()
        i.circy += i.speed
        if i.circy > height + 30:
            ballist.remove(i)
            balls -= 1
    CANVAS.blit(play, position3Font)
    CANVAS.blit(fallDown, position5Font)






    if key[K_RETURN]:
        global menu
        menu = 2

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_m:

                    global soundCount3

                    soundCount3 += 1
                    if soundCount3 % 2 == 1:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == K_s:
                        global soundCount4
                        if soundCount4 != 0:
                            soundCount4 = 0
                        else:
                            soundCount4 = 1


def gameOver():
    CANVAS.fill(BLACK)

    highScoreFile = open("highscore.txt", 'r')
    highScore = highScoreFile.readline()
    highScore = int(highScore)
    if score > highScore:
        highScoreFile = open("highscore.txt", 'w')
        scoreString = str(score)
        highScoreFile.write(scoreString)
        global default
        default = ORANGE


    gameOverText = endFont.render("GAME OVER", True, WHITE)
    surfaceScore = scoreFont.render("Score: " + str(score), True, WHITE)
    surfaceHi = scoreFont.render("High Score: " + str(highScore), True, default)
    play = tedfont.render("Press Enter to Play Again", True, WHITE)

    positionFont = surfaceScore.get_rect()
    positionFont.center = (width/2, 300)
    CANVAS.blit(surfaceScore, positionFont)
    position2Font = gameOverText.get_rect()
    position2Font.center = (width - width/2, 150)
    CANVAS.blit(gameOverText, position2Font)
    position3Font = play.get_rect()
    position3Font.center = (width/2, 500)
    CANVAS.blit(play, position3Font)
    position4Font = surfaceHi.get_rect()
    position4Font.center = (width/2, 375)
    CANVAS.blit(surfaceHi, position4Font)


    if key[K_RETURN]:
        playAgain()
moml = 0
momr = 0
def playAgain():
    global score, speed, level, recty, rectx, recth, rectw, mx, my, walls, ballx, bally, doll

    score = 0
    speed = 1
    level = 100
    recty = height + 10
    rectx = 100
    recth = 10
    rectw = 300
    mx = 0
    my = 0
    ballx = 250
    bally = 50
    walls = []
    doll = 1




menu = 0
gameLoop = True
while gameLoop:

    if menu == 0:
        mainMenu()

    else:

        if speed == 3.2:
            CANVAS.fill((17, 107, 35))
            gemini = WHITE
        elif speed == 2.51:
            CANVAS.fill((38, 34, 143))
            gemini = GREEN
        elif speed == 2:
            CANVAS.fill(PURPLE)
            gemini = YELLOW
        else:
            CANVAS.fill((0, 0, 0))
            gemini = ORANGE

        textSurfaceObj = fontObj.render("Score: " + str(score), True, WHITE)
        textRectObj = (10, 10)
        CANVAS.blit(textSurfaceObj, textRectObj)



        #Move ball left or right
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and ballx > 20 and doll == 1:
            ballx -= 6
            if speed == 3.2:
                ballx -= 1
            moml += 1
        if key[pygame.K_RIGHT] and ballx < width - 20 and doll == 1:
            ballx += 6
            if speed == 3.2:
                ballx += 1
            momr += 1



        if moml > 0 and ballx > 30 and doll == 1:

            ballx -= (moml/10)
            moml -= .5

        if momr > 0 and ballx < width - 30 and doll ==1:

            ballx += (momr/10)
            momr -= .5

        frameCount += 1
        if frameCount % 10 == 0 and bally > 7:
            score += 1

        elif score > 1000:
            speed = 3.2
            level = 40
        elif score > 500:
            speed = 2.51
            level = 50
        elif score > 200:
            speed = 2
            level = 80
        elif score > 0:
            speed = 1
            level = 100

        collist = []
        for i, j in walls:

            if bally > 5:
                i.recty -= speed
                j.recty -= speed
            if detectCollisions(i.rectx, i.recty, i.rectw, i.recth, ballx, bally, rad, rad):
                collist.append(detectCollisions(i.rectx, i.recty, i.rectw, i.recth, ballx, bally, rad, rad))
                if i in hitdetect.keys():
                    pass
                else:
                    if bally < height - 20 and soundCount4 == 0:
                        hitsound.play()
                    hitdetect[i] = 0
            if detectCollisions(j.rectx, j.recty, j.rectw, j.recth, ballx, bally, rad, rad):
                collist.append(detectCollisions(j.rectx, j.recty, j.rectw, j.recth, ballx, bally, rad, rad))
                if j in hitdetect.keys():
                    pass
                else:
                    if bally < height - 20 and soundCount4 == 0:
                        hitsound.play()
                    hitdetect[j] = 0

        if len(collist) != 0:

            collision = True

        else:

            collision = False
        if bally < height - 30:
            soundCount = 0
        if bally >= height - 21 and soundCount == 0 and soundCount4 == 0:
            hitsound.play()
            soundCount = 1

        if bally <= height - 20 and not collision:
            bally += 8

        if collision:
            for i, t in walls:
                if detectCollisions(i.rectx, i.recty, i.rectw, i.recth, ballx, bally, rad, rad):
                    bally = i.recty - 17
                elif detectCollisions(t.rectx, t.recty, t.rectw, t.recth, ballx, bally, rad, rad):
                    bally = t.recty - 17
                else:
                    pass

        if frameCount % level == 0 or frameCount == 1:
            gapSize = 100
            gapLoc = random.randint(0, width - gapSize)
            secondWidth = width - (gapLoc + gapSize)
            walls.append((Rect(0, recty, gapLoc, recth), Rect(gapLoc + gapSize, recty, secondWidth, recth)))

        #pygame.draw.rect(CANVAS, ORANGE, (ballx, bally, 30, 30))
        pygame.draw.circle(CANVAS, gemini, (int(ballx), int(bally)), rad, 0)

        for i, j in walls:
            i.render()
            j.render()
            if bally > 5:
                i.recty -= 1
                j.recty -= 1

        if bally <= 5:
            doll = 0
            gameOver()

    for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_m:
                        soundCount3 += 1
                        if soundCount3 % 2 == 1:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    if event.key == K_s:
                        if soundCount4 != 0:
                            soundCount4 = 0
                        else:
                            soundCount4 = 1


    pygame.display.update()
    fpsClock.tick(FPS)
