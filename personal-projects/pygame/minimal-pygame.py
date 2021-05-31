import pygame


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game name')
        self.resolution = 640, 360
        self.application_surface = pygame.display.set_mode(self.resolution, flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        pass

    # logic of the game
    def update(self, delta_time):
        pass

    # drawing of the game
    def draw(self):
        pass

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
            self.application_surface.fill((0, 0, 0))
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    Game()
