import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x, y, radius)
        if hasattr(self, "containers"):
            self.add(*self.containers)

        # Create the surface
        size = self.radius * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Draw the initial circle
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, 2)

        # Set up movement
        speed = random.uniform(20, 100)
        angle = random.uniform(0, 360)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(speed, 0).rotate(angle)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            random_angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(random_angle)
            second_velocity = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_new_asteroid.velocity = first_velocity * 1.2
            second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_new_asteroid.velocity = second_velocity * 1.2

    def update(self, dt):
        # Update position
        self.position += self.velocity * dt
        self.rect.center = self.position