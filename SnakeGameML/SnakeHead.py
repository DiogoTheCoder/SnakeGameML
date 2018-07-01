class SnakeHead:
    """Represents the head of the Snake"""
    headX = 150
    headY = 150
    headPos = "S"
    snakeImage = "snake_head.png"
    speed = 10
    numOfMoves = 0
    lastSuggestedMove = []
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