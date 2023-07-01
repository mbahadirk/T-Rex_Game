import random


class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, vel):
        # Move the obstacle horizontally based on the given velocity
        self.x -= vel
        if self.x < -self.width:
            self.reset()

    def reset(self):
        # Reset the obstacle's position and width to random values
        self.x = random.randint(1000, 2000)
        self.width = random.randint(1, 3) * 40

    def collider(self):
        # Get the collision boundaries of the obstacle
        x_col = list(range(self.x, self.x + self.width))
        y_col = list(range(self.y, self.y + self.height))
        return [x_col, y_col]
