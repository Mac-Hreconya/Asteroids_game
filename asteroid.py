import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        # Generate random split angle between 20-50 degrees
        split_angle = random.uniform(20, 50)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new velocity vectors
        velocity1 = self.velocity.rotate(split_angle) * 1.2
        velocity2 = self.velocity.rotate(-split_angle) * 1.2
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        
        # Remove the original asteroid
        self.kill()