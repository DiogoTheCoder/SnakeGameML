import random
import sys
from SnakeHead import SnakeHead

class SnakeBot:
    """description of class"""
    
    #movements 25% per direction
    def randy(player):
        seed = []
        for i in range(1,20):
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
                        keyToPress.append("U")

                elif randomPos == 4:
                    if player.headPos != "N":
                        keyToPress.append("D")
                else:
                    print("INCORRECT RANDOM VALUE")

            seed.append([i, keyToPress])

        return seed


            
            
#time before next move

