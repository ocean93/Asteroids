import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        pygame.sprite.Sprite.__init__(self)
        
        size = PLAYER_RADIUS * 2
        self.image = pygame.Surface((size, size,), pygame.SRCALPHA)
        
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self._draw_triangle()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        center = pygame.Vector2(self.radius, self.radius)
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    
    def _draw_triangle(self):
        self.image.fill((0,0,0,0))
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self._draw_triangle()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = (int(self.position.x),int(self.position.y))



