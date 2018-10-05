from SnakeHead import SnakeHead

class SnakeBody():
    """Provides info on how long the snake is"""
    snakeImage = "snake.png"
    body = [(SnakeHead.headX,SnakeHead.headY-10), (SnakeHead.headX,SnakeHead.headY-20), (SnakeHead.headX, SnakeHead.headY-30)]


    #[[aX,aY],[bX,bY],[cX,cY]] = [[SnakeHead.headX,SnakeHead.headY], [aX,aY], [bX,bY]]
    #body[0][0] = SnakeHead.headX
    #body[0][1] = SnakeHead.headY
    #for i in range(1,len(body)):
   #     body[i]=body[i-1]
    