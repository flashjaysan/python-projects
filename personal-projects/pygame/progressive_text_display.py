import pygame


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Progressive text display')
        self.resolution = 640, 360
        self.display_surface = pygame.display.set_mode(self.resolution, flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.font = pygame.font.SysFont(None, 24)
        self.text = 'This is a test text to try things.'
        self.current_text_index = 0
        self.running = True
        self.main_loop()
        pygame.quit()

    # logic of the game
    def update(self, delta_time):
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
            self.timer += delta_time
            if self.timer > 0.2:
                self.current_text_index += 1
                if self.current_text_index < len(self.text) and self.text[self.current_text_index] == ' ':
                    self.current_text_index += 1
                if self.current_text_index >= len(self.text):
                    self.current_text_index = 0
                self.timer = 0
            text_to_display = self.text[:self.current_text_index]
            text_surface = self.font.render(text_to_display, True, 'white')

            # draw
            self.display_surface.fill('black')
            self.display_surface.blit(text_surface, (20, 20))
            pygame.display.update()


if __name__ == "__main__":
    Game()
