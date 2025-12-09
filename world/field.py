import pygame
import settings
import os

pygame.init()
clock = pygame.time.Clock()
screen = settings.screen
MAP_WIDTH = settings.MAP_WIDTH
MAP_HEIGHT = settings.MAP_HEIGHT
TILE_SIZE = settings.TILE_SIZE

field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

FIELD_OFFSET_X = 5
FIELD_OFFSET_Y = 5
CELL_SIZE = TILE_SIZE - 5  # если хочешь зазоры

# путь к картинке
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "img")
GROUND_PATH = os.path.join(IMG_DIR, "ground.png")
GRASS_PATH = os.path.join(IMG_DIR, "grass.png")
TREE_PATH = os.path.join(IMG_DIR, "tree.png")

ground_img = pygame.image.load(GROUND_PATH).convert_alpha()
ground_img = pygame.transform.scale(ground_img, (CELL_SIZE, CELL_SIZE))

grass_img = pygame.image.load(GRASS_PATH).convert_alpha()
grass_img = pygame.transform.scale(grass_img, (CELL_SIZE, CELL_SIZE))

tree_img = pygame.image.load(TREE_PATH).convert_alpha()
tree_img = pygame.transform.scale(tree_img, (CELL_SIZE, CELL_SIZE))

def field_draw():
    screen.fill("grey")

    height = len(field)
    width = len(field[0])

    for y in range(height):
        for x in range(width):
            tile = field[y][x]

            pixel_x = FIELD_OFFSET_X + x * TILE_SIZE
            pixel_y = FIELD_OFFSET_Y + y * TILE_SIZE

            rect = (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE)

            if tile == 0:
                screen.blit(ground_img, (pixel_x, pixel_y))
            elif tile == 1:
                screen.blit(ground_img, (pixel_x, pixel_y))
                screen.blit(grass_img, (pixel_x, pixel_y))
            elif tile == 2:
                screen.blit(ground_img, (pixel_x, pixel_y))
                screen.blit(tree_img, (pixel_x, pixel_y))
            else:
                pygame.draw.rect(screen, "black", rect)



