import random
import pygame

class Dino:
    def __init__(self, x, y, width, height, jump_height, is_jump, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump_height = jump_height
        self.jump_h = 15
        self.is_jump = is_jump
        self.color = list(color)
        self.is_rainbow = False  # New attribute to track rainbow effect
        self.x_col = []
        self.y_col = []

    def reset(self):
        self.x = 100
        self.y = 240
        self.is_jump = False
        self.jump_height = self.jump_h

    def rainbow(self):
        r, g, b = self.color[0], self.color[1], self.color[2]
        if self.is_rainbow:
            # Generate random RGB values
            red = random.randint(50, 200)
            green = random.randint(50, 200)
            blue = random.randint(50, 200)
            self.color = [red, green, blue]
        else:
            self.color = [r, g, b]

    def toggle_rainbow(self):
        self.is_rainbow = not self.is_rainbow

    def collider(self):
        self.x_col = [x for x in range(self.x, self.x + self.width)]
        self.y_col = [y for y in range(self.y, self.y + self.height)]
        return [self.x_col, self.y_col]

    def jump(self):
        if self.jump_height >= -self.jump_h:
            self.y -= self.jump_height
            self.jump_height -= 1
            self.x_col, self.y_col = [], []
            self.collider()
        else:
            self.is_jump = False
            self.jump_height = self.jump_h
