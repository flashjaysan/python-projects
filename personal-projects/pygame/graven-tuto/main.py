import pygame
import player


class Game:

    BACKGROUND_COLOR = pygame.color.Color((0, 0, 0))

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption('Comet Fall Game')
        self.resolution = 1080, 720
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
        self.background = pygame.image.load('assets/bg.jpg')
        self.player = player.Player()
        self.player.rect.centerx = 1080 / 2
        self.player.rect.y = 500
        self.sprite_group.add(self.player)

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
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()

            # update
            delta_time = self.clock.tick(self.BASE_FPS) / 1000
            self.update(delta_time)

            # draw
            self.display_surface.blit(self.background, (0, -200))
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    Game()
