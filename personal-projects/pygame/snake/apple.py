import pygame
import random


class Apple:

    LIGHT_RED = 231, 76, 60

    def __init__(self, tile_size, grid_width, grid_height, snake):
        self.tile_size = tile_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.new_position(snake)

    def new_position(self, snake):
        self.random_position()
        while self.position in snake.parts:
            self.random_position()

    def random_position(self):
        self.position = pygame.Vector2(random.randrange(self.grid_width), random.randrange(self.grid_height))

    def draw(self, display_surface):
        pygame.draw.rect(
            display_surface,
            Apple.LIGHT_RED,
            (
                self.position.x * self.tile_size,
                self.position.y * self.tile_size,
                self.tile_size,
                self.tile_size
            )
        )
