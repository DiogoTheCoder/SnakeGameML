import random
import sys
from SnakeHead import SnakeHead


class SnakeBot:
    """description of class"""

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


        #N += (thehead.headY/300) *  0.3
        #S += (1 - thehead.headY/300) * 0.3
        #W += (thehead.headX/300) *  0.3
        #E += (1 - thehead.headX/300) * 0.3

        if thehead.headX == 10:
            W -= 1.0
        # Heading Rightwards/Eastwards
        if thehead.headX == 290:
            E -= 1.0
        # Heading Southwards
        if  thehead.headY == 290:
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

        #dont eat yourself


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

