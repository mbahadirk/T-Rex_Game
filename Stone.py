import random
import pygame

class Stone:
    def __init__(self,screen, x, y, size, color, velocity):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.velocity = velocity
        self.screen = screen

    def move(self,yes):
        if yes:
            self.x -= self.velocity

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
