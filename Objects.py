import pygame


class Bullet:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), 4)

    def update(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep


class Cannon:
    def __init__(self, health, x, y, angle):
        self.health = health
        self.x = x
        self.y = y
        self.angle = angle

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, self.x+20, self.y+5)
        pygame.draw.rect(screen, "red", (self.x, self.y), 5)

    
    #beep boop I'm making a change