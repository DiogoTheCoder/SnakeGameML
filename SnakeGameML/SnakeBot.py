import random
import sys
from SnakeHead import SnakeHead


class SnakeBot:
    """description of class"""
    #add snake view
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

    def snakeView(theapple, thehead, thebody):
        #apple
        #border
        #snake body

        N = 0
        S = 0
        E = 0
        W = 0

        appleView = (theapple.x,theapple.y)
        headLoc = (thehead.headX,thehead.headY)

        #comparing head to border
        # Heading Leftwards/Westwards
        if thehead.headX == 10:
            W -= 1.0
        # Heading Rightwards/Eastwards
        if thehead.headX == 570:
            E -= 1.0
        # Heading Southwards
        if  thehead.headY == 570:
            S -= 1.0
        # Heading Northwards
        if thehead.headY == 10:
            N -= 1.0

        #comparing head to apple
        if headLoc[0] < appleView[0]:
            #needs to move right for apple
            E += 0.2
        if headLoc[0] > appleView[0]:
            #needs to move left for apple
            W += 0.2
        if headLoc[1] < appleView[1]:
            #needs to move down for apple
            S += 0.2
        if headLoc[1] > appleView[1]:
            #needs to move up for apple
            N += 0.2



        outputList = {'U':N,'D':S,'R':E,'L':W}
        outputList = sorted(outputList.items(), key=lambda x: x[1])

        print(outputList)

        if thehead.headPos == "N" and outputList[-1][0] == "D":
            return outputList[-2][0]
        if thehead.headPos == "S" and outputList[-1][0] == "U":
            return outputList[-2][0]
        if thehead.headPos == "E" and outputList[-1][0] == "L":
            return outputList[-2][0]
        if thehead.headPos == "W" and outputList[-1][0] == "R":
            return outputList[-2][0]
        else:
            return outputList[-1][0]
        #comparing head to body

            
#time before next move

