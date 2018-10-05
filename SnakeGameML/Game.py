from Apple import Apple
from SnakeHead import SnakeHead
from SnakeBody import SnakeBody
import SnakeBot
from pygame.locals import *
import pygame
import time
import os
import csv
import random

class Game():
    """Runs the main game"""
    windowWidth = 310
    windowHeight = 310

    borderRes = (300, 300)
    numOfPlayers = 0
    score = 0
    scorelist = []
    #borderImage = "border.png"

    def __init__(self, cnx=None):
        self._running = True
        self._displaySurface = None
        self._snakeHeadImageSurface = None
        self._snakeBodyImageSurface = None
        self._appleImageSurface = None
        #self._borderImageSurface = None
        self.thePlayer = SnakeHead()
        self.apple = Apple()
        self.cnx = cnx

    def on_init(self):
        pygame.init()
        self._displaySurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._snakeHeadImageSurface = pygame.image.load(SnakeHead.snakeImage).convert()
        self._snakeBodyImageSurface = pygame.image.load(SnakeBody.snakeImage).convert()
        self._appleImageSurface = pygame.image.load(Apple.appleImage).convert()
        #self._borderImageSurface = pygame.image.load(self.borderImage).convert()
        self._running = True
        #self.display_apple()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.renderToScreen()
    
    def renderToScreen(self):
        self._displaySurface.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        #self._displaySurface.blit(self._borderImageSurface, (0, 0))
        self._displaySurface.blit(self._snakeHeadImageSurface, (self.thePlayer.headX, self.thePlayer.headY))

        for x in range(len(SnakeBody.body)):
            self._displaySurface.blit(self._snakeBodyImageSurface, (SnakeBody.body[x][0], SnakeBody.body[x][1]))

        newBodyPos = []
        newBodyPos.append((self.thePlayer.headX,self.thePlayer.headY))

        for i in range(1, len(SnakeBody.body)):
            newBodyPos.append(SnakeBody.body[i - 1])

        SnakeBody.body = newBodyPos
        if (self.thePlayer.numOfMoves >= 500):
            self.dies()
        elif (self.thePlayer.headX >= 0 and self.thePlayer.headX <= self.borderRes[0]) and (self.thePlayer.headY >= 0 and self.thePlayer.headY <= self.borderRes[1]):
            for i in range(1,len(SnakeBody.body)):
                #print(self.thePlayer.headX,self.thePlayer.headY,i)

                if (self.thePlayer.headX,self.thePlayer.headY)!=SnakeBody.body[i]:
                    # Not dead - not hit border
                    self._displaySurface.blit(self._appleImageSurface, (self.apple.x, self.apple.y))
                    #print("apple",self.apple.x, self.apple.y, "player",self.thePlayer.headX, self.thePlayer.headY)
                    if (self.apple.x,self.apple.y)==(self.thePlayer.headX,self.thePlayer.headY):
                        self.apple.newLoc(self.thePlayer, SnakeBody.body)
                        self.score+=1

                        # EAT APPLE - GROW
                        SnakeBody.body.append(SnakeBody.body[-1])

                        #print(SnakeBody.body)

                    #self._displaySurface.blit(text, (300, 300))
                    self._displaySurface.blit(text,
                    (100 - text.get_width() // 2, 100 - text.get_height() // 2))


                else:
                    print("DEAD - ATE ITSELF    SCORE - " + str(self.score) + "    BRANDON'S BIAS P - " + str(SnakeBot.appleB))
                    self.dies()
                    break
        else:
            print("DEAD - HIT BORDER    SCORE - " + str(self.score) + "    BRANDON'S BIAS P - " + str(SnakeBot.appleB))
            self.dies()
            
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False or self.thePlayer.deathCount >= 1:
            self._running = False
        #seedAndKeys = SnakeBot.randy(self.thePlayer)

        #for x in range(100):
        #    pygame.event.pump()
        #    self.thePlayer.move()
        #    keys = pygame.key.get_pressed()
        #    view = SnakeBot.snakeView2(self.apple, self.thePlayer, SnakeBody.body)
            
        #    self.on_loop()
        #    self.on_render()
        #    time.sleep(10/1000)
        #    self.changePlayerFacing(keys, view)

        for x in range(11):
            SnakeBot.bodyB = float(x / 10)

            while (self.thePlayer.deathCount < 3 and self._running):
                pygame.event.pump()
                self.thePlayer.move()
                keys = pygame.key.get_pressed()
                view = SnakeBot.snakeView2(self.apple, self.thePlayer, SnakeBody.body)
                
                self.changePlayerFacing(keys, view)
                self.thePlayer.numOfMoves += 1
                self.on_loop()
                self.on_render()
                time.sleep(100/1000)
                
            
            #SnakeBot.appleB -= 0.1
            self.thePlayer.deathCount = 0
                
            #self.changeplayerfacing(keys, keyaipressed)

        if self._running == False:
            self.on_cleanup()

    def changePlayerFacing(self, keys, keyAIPressed):
        #print(keyAIPressed)
        try:
            if (keys[K_RIGHT] or keyAIPressed == "R"):
                if self.thePlayer.headPos != "W":
                    self.thePlayer.changeFacing("E")
                #self.thePlayer.moveRight()

            if (keys[K_LEFT] or keyAIPressed == "L"):
                if self.thePlayer.headPos != "E":
                    self.thePlayer.changeFacing("W")
                #self.thePlayer.moveLeft()

            if (keys[K_UP] or keyAIPressed == "U"):
                if self.thePlayer.headPos != "S":
                    self.thePlayer.changeFacing("N")

            if (keys[K_DOWN] or keyAIPressed == "D"):
                if self.thePlayer.headPos != "N":
                    self.thePlayer.changeFacing("S")

            if (keys[K_ESCAPE]):
                self._running = False

        except TypeError:
            print("TypeError!")

    def dies(self):
        if self.cnx != None:
            cursor = self.cnx.cursor()
            add_data = ("INSERT INTO scores "
                   "(num_of_moves, score, apple_b, body_b) "
                   "VALUES (%s, %s, %s, %s)")
            snake_data = (self.thePlayer.numOfMoves, self.score, SnakeBot.appleB, float(SnakeBot.bodyB))

            cursor.execute(add_data, snake_data)
            self.cnx.commit()
            cursor.close()

        self.thePlayer.deathCount += 1
        
        # FOR AI
        self.thePlayer.headX = random.randint(5, 30)*10
        self.thePlayer.headY = random.randint(5, 30)*10
        self.thePlayer.headPos = "S"
        SnakeBody.body = [(self.thePlayer.headX,self.thePlayer.headY-10), (self.thePlayer.headX,self.thePlayer.headY-20), (self.thePlayer.headX, self.thePlayer.headY-30)]
        self.thePlayer.numOfMoves = 0
        self.score = 0