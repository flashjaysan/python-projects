import pygame


class Snake:

    LIGHT_BLUE = 52, 152, 219
    DARK_BLUE = 41, 128, 185

    def __init__(self, tile_size, grid_width, grid_height):
        self.tile_size = tile_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        x = self.grid_width / 2
        y = self.grid_height / 2
        self.parts = [pygame.math.Vector2(x - 1, y), pygame.math.Vector2(x, y)]
        self.direction = pygame.math.Vector2(1, 0)
        self.move_delay = 0.2
        self.counter = 0
        self.moving = False

    def update(self, delta_time):
        self.counter += delta_time
        if self.counter > self.move_delay:
            self.moving = True
            self.counter = 0

    def move(self):
        self.parts.append(self.parts[-1] + self.direction)
        self.moving = False

    def eat(self, apple):
        head = self.parts[-1]
        return head == apple.position

    def remove_tail(self):
        if self.counter == 0:
            self.parts.pop(0)

    def is_colliding(self):
        head = self.parts[-1]
        body = self.parts[:-1]
        return head in body or head.x < 0 or head.x >= self.grid_width or head.y < 0 or head.y >= self.grid_height

    def set_direction(self, direction):
        if direction.x != 0 and direction.x != -self.direction.x or direction.y != 0 and direction.y != -self.direction.y:
            self.direction = direction

    def draw(self, display_surface):
        self.draw_head(display_surface)
        self.draw_body(display_surface)

    def draw_head(self, display_surface):
        head = self.parts[-1]
        pygame.draw.rect(
            display_surface,
            Snake.DARK_BLUE,
            (
                head.x * self.tile_size,
                head.y * self.tile_size,
                self.tile_size,
                self.tile_size
            )
        )

    def draw_body(self, display_surface):
        body = self.parts[:-1]
        for part in body:
            pygame.draw.rect(
                display_surface,
                Snake.LIGHT_BLUE,
                (
                    part.x * self.tile_size,
                    part.y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
            )
