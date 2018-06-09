#from Game import Game
import random

class Apple():
    """The food a snake eats, apparently"""
    x = 0
    y = 0
    appleImage = "apple.png"

    def __init__(self):
        self.newLoc()

    def newLoc(self):
        self.x = random.randint(0, 600 - 20)
        self.y = random.randint(0, 600 - 20)