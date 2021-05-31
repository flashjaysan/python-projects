import pygame
import standard_colors


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame window')
        dimensions = 640, 360
        self.application_surface = pygame.display.set_mode(dimensions)
        self.background_color = standard_colors.YELLOW

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_r:
                        self.background_color = standard_colors.RED
                    elif event.key == pygame.K_g:
                        self.background_color = standard_colors.GREEN

            self.application_surface.fill(self.background_color)
            pygame.display.update()


if __name__ == "__main__":
    Game()
