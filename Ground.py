import pygame

class Ground:
    def __init__(self, screen, height, vel):
        self.height = height
        self.vel = vel
        self.screen = screen
        self.color = (200, 180, 200)

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (0, self.screen.get_height() - self.height, self.screen.get_width(), self.height))
