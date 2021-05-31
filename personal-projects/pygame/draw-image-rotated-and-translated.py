import pygame
import vector2
import math


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Bouncing image')
        self.resolution_width = 640
        self.resolution_height = 360
        self.application_surface = pygame.display.set_mode((self.resolution_width, self.resolution_height), flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.image = pygame.image.load('cat.jpg')
        self.angle = 0
        self.position = vector2.Vector2()
        self.head_position = (86 - 150, 114 - 200)
        self.head_angle_to_center = math.atan2(self.head_position[1], self.head_position[0])
        self.head_distance_to_center = math.sqrt(self.head_position[0] ** 2 + self.head_position[1] ** 2)
        self.initialize()
        self.running = True
        self.main_loop()
        pygame.quit()

    # called each time the game restarts
    def initialize(self):
        pass

    # logic of the game
    def update(self, delta_time):
        self.angle += 50 * delta_time

    # drawing of the game
    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.position.x = (self.resolution_width - rotated_image.get_width()) / 2 - math.cos(math.radians(self.angle) + self.head_angle_to_center) * self.head_distance_to_center
        self.position.y = (self.resolution_height - rotated_image.get_height()) / 2 - math.sin(math.radians(self.angle) + self.head_angle_to_center) * self.head_distance_to_center
        self.application_surface.blit(rotated_image, self.position.to_tuple())

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
