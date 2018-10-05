import random

class SnakeHead:
    """Represents the head of the Snake"""
    headX = random.randint(5, 30)*10
    headY = random.randint(5, 30)*10
    headPos = "S"
    snakeImage = "snake_head.png"
    speed = 10
    numOfMoves = 0
    lastSuggestedMove = []
    deathCount = 0
    #body = SnakeBody()

    def move(self):
        if self.headPos == "N":
            self.headY = self.headY - self.speed

        elif self.headPos == "S":
            self.headY = self.headY + self.speed

        elif self.headPos == "E":
            self.headX = self.headX + self.speed

        elif self.headPos == "W":
            self.headX = self.headX - self.speed

    def changeFacing(self, newPos):
        self.headPos = newPos

    #def eatApple(self):
       # GROW!
       # self.body.length += 1