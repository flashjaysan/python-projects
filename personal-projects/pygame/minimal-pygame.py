import pygame


class Game:

    BACKGROUND_COLOR = pygame.color.Color((0, 0, 0))

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Game name')
        self.resolution = 640, 360
        self.display_surface = pygame.display.set_mode(self.resolution, flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.sprite_group = pygame.sprite.Group()
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.mixer.quit()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        pass

    # logic of the game
    def update(self, delta_time):
        self.sprite_group.update(delta_time)

    # drawing of the game
    def draw(self):
        self.sprite_group.draw(self.display_surface)

    def main_loop(self):
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # update
            delta_time = self.clock.tick(self.BASE_FPS) / 1000
            self.update(delta_time)

            # draw
            self.display_surface.fill(Game.BACKGROUND_COLOR)
            self.draw()
            pygame.display.update() # or pygame.display.flip()


if __name__ == "__main__":
    Game()
