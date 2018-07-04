#from Game import Game
import random

class Apple():
    """The food a snake eats, apparently"""
    x = random.randrange(10, 290, 10)
    y = random.randrange(10, 290, 10)
    appleImage = "apple.png"

    def newLoc(self, thePlayer, playerBody):
        #random.seed( 100 )
        
        self.x = random.randrange(10, 290, 10)
        self.y = random.randrange(10, 290, 10)

        if self.x == thePlayer.headX and self.y == thePlayer.headY:
            self.newLoc(thePlayer, playerBody)

        for body in playerBody:
            if (self.x, self.y) == body:
                self.newLoc(thePlayer, playerBody)