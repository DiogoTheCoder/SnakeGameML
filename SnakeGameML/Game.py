from Apple import Apple
from SnakeHead import SnakeHead
from SnakeBody import SnakeBody
from SnakeBot import SnakeBot
from pygame.locals import *
import pygame
import time
import os

class Game():
    """Runs the main game"""
    windowWidth = 800
    windowHeight = 600
    borderRes = (580, 580)
    numOfPlayers = 0
    score = 0
    borderImage = "border.png"

    def __init__(self):
        self._running = True
        self._displaySurface = None
        self._snakeHeadImageSurface = None
        self._snakeBodyImageSurface = None
        self._appleImageSurface = None
        self._borderImageSurface = None
        self.thePlayer = SnakeHead()
        self.apple = Apple()

    def on_init(self):
        pygame.init()
        self._displaySurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self._snakeHeadImageSurface = pygame.image.load(SnakeHead.snakeImage).convert()
        self._snakeBodyImageSurface = pygame.image.load(SnakeBody.snakeImage).convert()
        self._appleImageSurface = pygame.image.load(Apple.appleImage).convert()
        self._borderImageSurface = pygame.image.load(self.borderImage).convert()
        self._running = True
        #self.display_apple()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._displaySurface.fill((0, 0, 0))

        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))

        self._displaySurface.blit(self._borderImageSurface, (0, 0))
        self._displaySurface.blit(self._snakeHeadImageSurface, (self.thePlayer.headX, self.thePlayer.headY))

        for x in range(len(SnakeBody.body)):
            self._displaySurface.blit(self._snakeBodyImageSurface, (SnakeBody.body[x][0], SnakeBody.body[x][1]))

        newBodyPos = []
        newBodyPos.append((self.thePlayer.headX,self.thePlayer.headY))

        for i in range(1, len(SnakeBody.body)):
            newBodyPos.append(SnakeBody.body[i - 1])

        SnakeBody.body = newBodyPos

        if (self.thePlayer.headX > 0 and self.thePlayer.headX < self.borderRes[0]) and (self.thePlayer.headY > 0 and self.thePlayer.headY < self.borderRes[1]):
            for i in range(1,len(SnakeBody.body)):
                #print(self.thePlayer.headX,self.thePlayer.headY,i)
                if (self.thePlayer.headX,self.thePlayer.headY)!=SnakeBody.body[i]:
                    # Not dead - not hit border
                    self._displaySurface.blit(self._appleImageSurface, (self.apple.x, self.apple.y))
                    #print("apple",self.apple.x, self.apple.y, "player",self.thePlayer.headX, self.thePlayer.headY)
                    if self.apple.x-self.thePlayer.headX<=10 and self.apple.x-self.thePlayer.headX>=-10 and self.apple.y-self.thePlayer.headY<=10 and self.apple.y-self.thePlayer.headY>=-10:
                        #print("eaten")
                        self.apple.newLoc()
                        self.score+=1

                        # EAT APPLE - GROW
                        SnakeBody.body.append(SnakeBody.body[-1])

                        #print(SnakeBody.body)

                    #self._displaySurface.blit(text, (300, 300))
                    self._displaySurface.blit(text,
                    (320 - text.get_width() // 2, 240 - text.get_height() // 2))
                else:
                    self._running = False
        else:
            self._running = False

        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            self.thePlayer.move()
            keys = pygame.key.get_pressed()

            keyAI = SnakeBot.randy(self.thePlayer)

            for key in keyAI:
                self.changePlayerFacing(keys, key)


            keyAIPressed = "None"
            self.changePlayerFacing(keys, keyAIPressed)

            self.on_loop()
            self.on_render()
            
            time.sleep(100.0 / 1000.0)

        self.on_cleanup()

    def changePlayerFacing(self, keys, keyAIPressed):
        try:
            if (keys[K_RIGHT] or keyAIPressed == "R"):
                if self.thePlayer.headPos != "W":
                    self.thePlayer.changeFacing("E")
                #self.thePlayer.moveRight()

            if (keys[K_LEFT] or keyAIPressed == "L"):
                if self.thePlayer.headPos != "E":
                    self.thePlayer.changeFacing("W")
                #self.thePlayer.moveLeft()

            if (keys[K_UP] or keyAIPressed == "UP"):
                if self.thePlayer.headPos != "S":
                    self.thePlayer.changeFacing("N")

            if (keys[K_DOWN] or keyAIPressed == "DOWN"):
                if self.thePlayer.headPos != "N":
                    self.thePlayer.changeFacing("S")

            if (keys[K_ESCAPE]):
                self._running = False

        except TypeError:
            print("TypeError!")