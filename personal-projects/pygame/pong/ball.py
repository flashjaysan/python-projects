import pygame


class Ball(pygame.sprite.Sprite):

    color = 255, 255, 255

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Ball.color)
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def draw(self):
        pass
