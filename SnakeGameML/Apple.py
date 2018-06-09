#from Game import Game
import random

class Apple():
    """description of class"""
    x = 0
    y = 0
    appleImage = "apple.png"



    def __init__(self):
        self.newLoc()

    def newLoc(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)