import random
import sys
from SnakeHead import SnakeHead

class SnakeBot:
    """description of class"""
    
    #movements 25% per direction
    def randy(player):
        for i in range(20):
            random.seed( i )
            keyToPress = []
            for j in range(50):
                randomPos = random.randint(1,4)

                if randomPos == 1:
                    if player.headPos != "W":
                        keyToPress.append("R")

                elif randomPos == 2:
                    if player.headPos != "E":
                        keyToPress.append("L")

                elif randomPos == 3:
                    if player.headPos != "S":
                        keyToPress.append("UP")

                elif randomPos == 4:
                    if player.headPos != "N":
                        keyToPress.append("DOWN")
                else:
                    print("INCORRECT RANDOM VALUE")

            return keyToPress
            
#time before next move

