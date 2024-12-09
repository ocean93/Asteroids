import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.velocity = pygame.Vector2(0, 0)
        if hasattr(self, "containers"):
            self.add(*self.containers)

        size = SHOT_RADIUS * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)   

    def update(self, dt):
        super().update(dt)
        self.rect.center = self.position
        self.position += self.velocity * dt