import pygame
import sys
import time
import vector2

WIDTH = 640
HEIGHT = 360
DIMENSIONS = WIDTH, HEIGHT
TILE_SIZE = 40


def main():
    errors = pygame.init() # initialise pygame
    if errors[1] > 0:
        print('Initialisation failed.')
        sys.exit(-1)
    surface = pygame.display.set_mode(DIMENSIONS) # crée une surface
    pygame.display.set_caption('Snake') # modifie le titre de la fenêtre
    time.sleep(2) # attend 2 secondes
    red = pygame.Color(255, 0, 0) # créer une couleur RGB
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    brown = pygame.Color(165, 42, 42)
    
    fps_controller = pygame.time.Clock()
    head = vector2.Vector2(WIDTH / 2, HEIGHT / 2)
    body = []
    food = vector2.Vector2(random.randrange(int(WIDTH / TILE_SIZE)) * TILE_SIZE, random.randrange(int(HEIGHT / TILE_SIZE)) * TILE_SIZE)


def game_over():
    font = pygame.font.SysFont('Arial', 72)
    antialiasing = False
    color = red
    surface = font.render('GAME OVER', antialiasing, color)


main()
