import random, sys, numpy, math
from SnakeHead import SnakeHead
import Game

appleB = 0.0
bodyB = 0.5


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

    # Comparing head to border
    # Heading Leftwards/Westwards


    #N += (thehead.headY/300) *  0.3
    #S += (1 - thehead.headY/300) * 0.3
    #W += (thehead.headX/300) *  0.3
    #E += (1 - thehead.headX/300) * 0.3
        
    if thehead.headX == thehead.speed:
        W -= 1.0
    # Heading Rightwards/Eastwards
    if thehead.headX == Game.Game.borderRes[0] - thehead.speed:
        E -= 1.0
    # Heading Southwards
    if  thehead.headY == Game.Game.borderRes[0] - thehead.speed:
        S -= 1.0
    # Heading Northwards
    if thehead.headY == thehead.speed:
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


def snakeView2(theapple, thehead, thebody):
    suggestedDirection = [1, 1, 1, 1] # Directions = N, S, E, W
    headLoc = (thehead.headX,thehead.headY)
    appleView = (theapple.x,theapple.y)

    if thehead.headPos == "N":
        suggestedDirection[1] = 0
        suggestedDirection = calculateWeights(suggestedDirection, theapple, thebody, thehead)
    if thehead.headPos == "S":
        suggestedDirection[0] = 0
        suggestedDirection = calculateWeights(suggestedDirection, theapple, thebody, thehead)
    if thehead.headPos == "E":
        suggestedDirection[3] = 0
        suggestedDirection = calculateWeights(suggestedDirection, theapple, thebody, thehead)
    if thehead.headPos == "W":
        suggestedDirection[2] = 0
        suggestedDirection = calculateWeights(suggestedDirection, theapple, thebody, thehead)


    thehead.lastSuggestedMove = suggestedDirection
    direction = duplicateCheck(suggestedDirection.index(max(suggestedDirection)), suggestedDirection)

    if direction == 0:
        return "U"
    elif direction == 1:
        return "D"
    elif direction == 2:
        return "R"
    elif direction == 3:
        return "L"

def duplicateCheck(valueIdx, array):
    if (array.count(valueIdx) > 1):
        choice = random.randrange(len(array))
        if array[choice] == valueIdx:
            return choice
        else: 
            return duplicateCheck(valueIdx, array)
    else:
        return valueIdx

def wallCheck(suggestedDirection, thehead):

    if thehead.headX - thehead.speed == 0:
        suggestedDirection[3] = 0
    if thehead.headX + thehead.speed == 300:
        suggestedDirection[2] = 0
    if thehead.headY - thehead.speed == 0:
        suggestedDirection[0] = 0
    if thehead.headY + thehead.speed == 300:
        suggestedDirection[1] = 0

    return suggestedDirection        

def bodyCheck(suggestedDirection, thebody, thehead):
    for i in thebody:
        if (thehead.headX - thehead.speed, thehead.headY) == i:
            suggestedDirection[3] -= 1
        if (thehead.headX + thehead.speed, thehead.headY) == i:
            suggestedDirection[2] -= 1
        if (thehead.headX, thehead.headY - thehead.speed) == i:
            suggestedDirection[0] -= 1
        if (thehead.headX, thehead.headY + thehead.speed) == i:
            suggestedDirection[1] -= 1
    return suggestedDirection

def uPatternCheck(suggestedDirection, thebody, thehead):
    shortview = [
        (thehead.headX-10,thehead.headY-10),(thehead.headX+10,thehead.headY-10),
        (thehead.headX-10,thehead.headY+10),(thehead.headX+10,thehead.headY+10)
        ]
    
    if thehead.headPos == "N":
        if (shortview[0] in thebody) and (shortview[1] in thebody):
            suggestedDirection[0] -= bodyB
    if thehead.headPos == "S":
        if (shortview[2] in thebody) and (shortview[3] in thebody):
            suggestedDirection[1] -= bodyB
    if thehead.headPos == "E":
        if (shortview[1] in thebody) and (shortview[3] in thebody):
            suggestedDirection[2] -= bodyB
    if thehead.headPos == "W":
        if (shortview[0] in thebody) and (shortview[2] in thebody):
            suggestedDirection[3] -= bodyB

    return suggestedDirection

def calculateWeights(suggestedDirection, theapple, thebody, thehead):
    suggestedDirection = wallCheck(suggestedDirection, thehead)
    suggestedDirection = bodyCheck(suggestedDirection, thebody, thehead)
    suggestedDirection = calculateDirectionAngle(suggestedDirection, theapple, thehead, thebody)
    suggestedDirection = uPatternCheck(suggestedDirection, thebody, thehead)
    return suggestedDirection

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def calculateDirectionAngle(suggestedDirection, apple, head, body):
    # Directions = N, S, E, W
    snake = [[head.headX, head.headY], [body[0][0], body[0][1]]]
    a_vector = [0, -20]
    a = a_vector / numpy.linalg.norm(a_vector)

    apple = [apple.x, apple.y]
    b_vector = numpy.array(apple) - numpy.array(snake[0])
    b = b_vector / numpy.linalg.norm(b_vector)

    direction = math.atan2(a[0] * b[1] - a[1] * b[0], a[0] * b[0] + a[1] * b[1]) / math.pi

    # North-East Quadrant
    if direction >= 0 and direction < 0.5:
        suggestedDirection[0] += (1 - (direction / 0.5)) * appleB
        suggestedDirection[2] += (direction / 0.5) * appleB

    # South-East Quadrant
    if direction >= 0.5 and direction < 1:
        suggestedDirection[2] += (2 - (direction / 0.5)) * appleB
        suggestedDirection[1] += ((direction / 0.5) - 1) * appleB

    # South-West Quadrant
    if direction >= -1 and direction < -0.5:
        suggestedDirection[1] += -(1 + (direction / 0.5)) * appleB
        suggestedDirection[3] += ((direction / 0.5) + 2) * appleB

    # North-West Quadrant
    if direction >= -0.5 and direction < 0:
        suggestedDirection[0] += (1 + (direction / 0.5)) * appleB
        suggestedDirection[3] += -(direction / 0.5) * appleB

    return suggestedDirection
