#from Game import Game
import random

class Apple():
    """The food a snake eats, apparently"""
    x = 50
    y = 25
    appleImage = "apple.png"

    def newLoc(self, thePlayer, playerBody):
        #random.seed( 100 )
        
        self.x = random.randrange(0, 600 - 20, 10)
        self.y = random.randrange(0, 600 - 20, 10)

        if self.x == thePlayer.headX and self.y == thePlayer.headY:
            newLoc(self, thePlayer, playerBody)

        for body in playerBody:
            if (self.x, self.y) == body:
                newLoc(self, thePlayer, playerBody)