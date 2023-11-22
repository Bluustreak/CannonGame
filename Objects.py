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
        # the accelerations can be replaced by something more dynamic, 
        # in the case of multiple acceleration sources like wind or other bodies
        accx=0
        accy=1

        #the formula for displacement over time including acceleration
        prevx = self.x
        prevy = self.y
        self.x = self.x + self.vx * timestep + 0.5*accx*timestep**2
        self.y = self.y + self.vy * timestep + 0.5*accy*timestep**2
        self.vx = (self.x-prevx)/timestep
        self.vy = (self.y-prevy)/timestep
        #print(self.x, self.y)


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