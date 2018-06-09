import random
import sys
class SnakeBot(object):
    """description of class"""
    
    for i in range(20):
        randy(i)
    #movements 25% per direction
    def randy(x):
        random.seed( x )
        while true:
            if random.randint(1,4) == 1:
                self.thePlayer.changeFacing("E")
            elif random.randint(1,4) == 2:
                self.thePlayer.changeFacing("W")
            elif random.randint(1,4) == 3:
                self.thePlayer.changeFacing("N")
            else:
                self.thePlayer.changeFacing("S")
            

    #time before next move

