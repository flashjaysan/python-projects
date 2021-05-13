import pygame


def main():
    pygame.init()
    pygame.display.set_caption('Pygame window')
    dimensions = 640, 360
    screen = pygame.display.set_mode(dimensions)
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    main()
