import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.max_velocity = 5
        self.current_velocity = 0
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
    
    def move_right(self):
        self.current_velocity = self.max_velocity
    
    def move_left(self):
        self.current_velocity = -self.max_velocity
    
    def update(self, delta_time):
        self.rect.x -= self.current_velocity * delta_time
        
