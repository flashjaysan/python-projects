import pygame
import math


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rotating image with origin offset')
        self.resolution_width = 640
        self.resolution_height = 360
        self.application_surface = pygame.display.set_mode((self.resolution_width, self.resolution_height),
                                                           flags=pygame.SCALED)
        self.BASE_FPS = 60
        self.clock = pygame.time.Clock()
        self.image = pygame.Surface((200, 100), flags=pygame.SRCALPHA)
        self.image.fill((255, 0, 0))
        self.angle = 0
        self.position = [0, 0]
        self.anchor_point = (25, 75)
        self.image.set_at(self.anchor_point, (255, 255, 255))
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
        center_of_screen = (self.application_surface.get_width() // 2, self.application_surface.get_height() // 2)
        blit_with_rotation_around_point(self.image, self.application_surface, self.anchor_point, center_of_screen,
                                        self.angle)

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


def blit_with_rotation_around_point(src_img, dest_surface, origin_pos_in_src, dest_pos, angle):
    """
        src_img: the image to draw
        dest_surface: the surface to draw on
        origin_pos_in_src: the center of rotation of src_img
        dest_pos: the position in dest_surface where origin_pos_in_src should end up
        angle: the rotation in degrees
    """
    center_pos = pygame.Vector2(src_img.get_width() / 2, src_img.get_height() / 2)
    origin_to_center = pygame.Vector2(origin_pos_in_src[0] - center_pos[0], origin_pos_in_src[1] - center_pos[1])
    rotated_center_to_origin = origin_to_center.rotate(-angle)

    rotated_image = pygame.transform.rotate(src_img, angle)
    draw_pos = (round(dest_pos[0] - rotated_image.get_width() / 2 - rotated_center_to_origin.x),
                round(dest_pos[1] - rotated_image.get_height() / 2 - rotated_center_to_origin.y))
    dest_surface.blit(rotated_image, draw_pos)


if __name__ == "__main__":
    Game()
