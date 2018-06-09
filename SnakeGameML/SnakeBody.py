from SnakeHead import SnakeHead

class SnakeBody():
    """description of class"""
    snakeImage = "snake.png"
    body = [(100,75), (100,50), (100, 25)]


    #[[aX,aY],[bX,bY],[cX,cY]] = [[SnakeHead.headX,SnakeHead.headY], [aX,aY], [bX,bY]]
    #body[0][0] = SnakeHead.headX
    #body[0][1] = SnakeHead.headY
    #for i in range(1,len(body)):
   #     body[i]=body[i-1]
    