import pygame
import random


class Game:

    LIGHT_GREEN = 26, 188, 156
    LIGHT_BLUE = 52, 152, 219
    DARK_BLUE = 41, 128, 185
    LIGHT_RED = 231, 76, 60

    TILE_SIZE = 20

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Snake')
        self.resolution = 640, 360
        self.display_surface = pygame.display.set_mode(self.resolution)#, flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.sprite_group = pygame.sprite.Group()
        self.sound_move = pygame.mixer.Sound('assets/sounds/move.wav')
        self.sound_eat = pygame.mixer.Sound('assets/sounds/eat.wav')
        self.sound_hurt = pygame.mixer.Sound('assets/sounds/hurt.wav')
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.mixer.quit()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        self.snake = [pygame.math.Vector2(15, 9), pygame.math.Vector2(16, 9)]
        self.direction = pygame.math.Vector2(1, 0)
        self.move_delay = 0.2
        self.counter = 0
        self.apple = pygame.math.Vector2(random.randint(0, 31), random.randint(0, 17))
        while self.apple in self.snake:
            self.apple = pygame.math.Vector2(random.randint(0, 31), random.randint(0, 17))

    # logic of the game
    def update(self, delta_time):
        self.counter += delta_time
        if self.counter > self.move_delay:
            self.snake.append(self.snake[-1] + self.direction)
            if self.snake[-1] == self.apple:
                while self.apple in self.snake:
                    self.apple = pygame.math.Vector2(random.randint(0, 31), random.randint(0, 17))
                pygame.mixer.stop()
                self.sound_eat.play()
            else:
                self.snake.pop(0)
                pygame.mixer.stop()
                self.sound_move.play()
            self.counter = 0
        if self.snake[-1] in self.snake[:-1] or self.snake[-1].x < 0 or self.snake[-1].x > 31 or  self.snake[-1].y < 0 or self.snake[-1].y > 17:
            pygame.mixer.stop()
            self.sound_hurt.play()
            self.initialize()

    # drawing of the game
    def draw(self):
        self.draw_snake_part()
        self.draw_snake_head()
        self.draw_apple()

    def draw_snake_part(self):
        snake_body = self.snake[:-1]
        for snake_part in snake_body:
            pygame.draw.rect(
                self.display_surface,
                Game.LIGHT_BLUE,
                (
                    snake_part[0] * Game.TILE_SIZE,
                    snake_part[1] * Game.TILE_SIZE,
                    Game.TILE_SIZE,
                    Game.TILE_SIZE
                )
            )

    def draw_snake_head(self):
        pygame.draw.rect(
            self.display_surface,
            Game.DARK_BLUE,
            (
                self.snake[-1][0] * Game.TILE_SIZE,
                self.snake[-1][1] * Game.TILE_SIZE,
                Game.TILE_SIZE,
                Game.TILE_SIZE
            )
        )

    def draw_apple(self):
        pygame.draw.rect(
            self.display_surface,
            Game.LIGHT_RED,
            (
                self.apple[0] * Game.TILE_SIZE,
                self.apple[1] * Game.TILE_SIZE,
                Game.TILE_SIZE,
                Game.TILE_SIZE
            )
        )

    def main_loop(self):
        while self.running:
            new_direction = pygame.Vector2()
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_UP:
                        new_direction = pygame.Vector2(0, -1)
                    if event.key == pygame.K_DOWN:
                        new_direction = pygame.Vector2(0, 1)
                    if event.key == pygame.K_LEFT:
                        new_direction = pygame.Vector2(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        new_direction = pygame.Vector2(1, 0)

            if new_direction.x != 0 and new_direction.x != -self.direction.x or new_direction.y != 0 and new_direction.y != -self.direction.y:
                self.direction = new_direction

            # update
            delta_time = self.clock.tick(self.BASE_FPS) / 1000
            self.update(delta_time)

            # draw
            self.display_surface.fill(Game.LIGHT_GREEN)
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    Game()
