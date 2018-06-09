#from Game import Game
import random

class Apple():
    """description of class"""
    x = 0
    y = 0
    appleImage = "apple.png"

    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

        self.x = 30
        self.y = 30