import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def collision(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        if distance <= self.radius + other_shape.radius:
            return True
        else:
            return False

    def update(self, dt):
        pass