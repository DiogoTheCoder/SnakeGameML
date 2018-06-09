from Apple import Apple
from Player import Player
from pygame.locals import *
import pygame
import time
import os

class Game():
    """description of class"""
    windowWidth = 800
    windowHeight = 600
    numOfPlayers = 0
    score = 0
    def __init__(self):
        self._running = True
        self._displaySurface = None
        self._snakeImageSurface = None
        self.thePlayer = Player()
        self.apple = Apple()

    def on_init(self):
        pygame.init()
        self._displaySurface = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        print("TEST!")
        print(os.getcwd())
        self._snakeImageSurface = pygame.image.load(Player.snakeImage).convert()
        self._running = True
        #self.display_apple()
        

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):


        self._displaySurface.fill((0, 0, 0))
        self._displaySurface.blit(self._snakeImageSurface, (self.thePlayer.x, self.thePlayer.y))
        self._displaySurface.blit(pygame.image.load(Apple.appleImage).convert(), (self.apple.x, self.apple.y))
        print("apple",self.apple.x, self.apple.y, "player",self.thePlayer.x, self.thePlayer.y)
        if self.apple.x-self.thePlayer.x<=10 and self.apple.x-self.thePlayer.x>=-10 and self.apple.y-self.thePlayer.y<=10 and self.apple.y-self.thePlayer.y>=-10:
            print("eaten")
            self.apple.newLoc()
            self.score+=1
        pygame.display.flip()

    def display_apple(self):
        apple = Apple()
        self._displaySurface.blit(pygame.image.load(Apple.appleImage).convert(), (apple.x, apple.y))
        print(apple.x, apple.y)
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

            if (keys[K_RIGHT]):
                self.thePlayer.changeFacing("E")
                #self.thePlayer.moveRight()

            if (keys[K_LEFT]):
                self.thePlayer.changeFacing("W")
                #self.thePlayer.moveLeft()

            if (keys[K_UP]):
                self.thePlayer.changeFacing("N")

            if (keys[K_DOWN]):
                self.thePlayer.changeFacing("S")

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)

        self.on_cleanup()

