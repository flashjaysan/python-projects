import pygame
import snake
import apple


class Game:

    LIGHT_GREEN = 26, 188, 156

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Snake')
        self.resolution = 640, 360
        self.display_surface = pygame.display.set_mode(self.resolution, flags=pygame.SCALED)
        self.tile_size = 40
        self.grid_width = self.resolution[0] / self.tile_size
        self.grid_height = self.resolution[1] / self.tile_size
        self.sound_move = pygame.mixer.Sound('assets/sounds/move.wav')
        self.sound_eat = pygame.mixer.Sound('assets/sounds/eat.wav')
        self.sound_hurt = pygame.mixer.Sound('assets/sounds/hurt.wav')
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.mixer.quit()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        self.snake = snake.Snake(self.tile_size, self.grid_width, self.grid_height)
        self.apple = apple.Apple(self.tile_size,  self.grid_width, self.grid_height, self.snake)

    # logic of the game
    def update(self, delta_time):
        self.snake.update(delta_time)
        if self.snake.moving:
            self.snake.move()
            if self.snake.eat(self.apple):
                self.apple.new_position(self.snake)
                pygame.mixer.stop()
                self.sound_eat.play()
            else:
                self.snake.remove_tail()
                pygame.mixer.stop()
                self.sound_move.play()

            if self.snake.is_colliding():
                pygame.mixer.stop()
                self.sound_hurt.play()
                self.initialize()

    # drawing of the game
    def draw(self):
        self.snake.draw(self.display_surface)
        self.apple.draw(self.display_surface)

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

            self.snake.set_direction(new_direction)

            # update
            delta_time = self.clock.tick(self.BASE_FPS) / 1000
            self.update(delta_time)

            # draw
            self.display_surface.fill(Game.LIGHT_GREEN)
            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    Game()
