import pygame
import vector2


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Bouncing image')
        self.resolution_width = 640
        self.resolution_height = 360
        self.application_surface = pygame.display.set_mode((self.resolution_width, self.resolution_height), flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load('wall.png')
        self.position = vector2.Vector2()
        self.velocity = vector2.Vector2(200, 180)
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        pass

    # logic of the game
    def update(self, delta_time):
        if self.position.x < 0 or self.position.x > self.resolution_width:
            self.velocity.x *= -1
        if self.position.y < 0 or self.position.y > self.resolution_height:
            self.velocity.y *= -1
        self.position += self.velocity * delta_time

    # drawing of the game
    def draw(self):
        self.application_surface.blit(self.image, self.position.to_tuple())

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
            self.application_surface.fill('black')
            self.draw()
            pygame.display.update()


if __name__ == "__main__":
    Game()
