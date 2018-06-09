class Player:
    """description of class"""
    x = 10
    y = 10
    speed = 10
    headPos = "S"
    snakeImage = "snake.png"

    def move(self):
        if self.headPos == "N":
            self.y = self.y - self.speed

        elif self.headPos == "S":
            self.y = self.y + self.speed

        elif self.headPos == "E":
            self.x = self.x + self.speed

        elif self.headPos == "W":
            self.x = self.x - self.speed

    def moveRight(self):
        self.x = self.x + self.speed
        print("Player: moved to the RIGHT")

    def moveLeft(self):
        self.x = self.x - self.speed
        print("Player: moved to the LEFT")

    def changeFacing(self, newPos):
        self.headPos = newPos