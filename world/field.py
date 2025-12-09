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

# время роста в секундах для каждой клетки
growth_time = [
    [0.0 for _ in range(len(field[0]))]
    for _ in range(len(field))
]

GROWTH_DURATION = 5.0  # секунд до полного размера
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

def field_draw(dt):
    screen.fill("grey")

    height = len(field)
    width = len(field[0])

    for y in range(height):
        for x in range(width):
            tile = field[y][x]

            pixel_x = FIELD_OFFSET_X + x * TILE_SIZE
            pixel_y = FIELD_OFFSET_Y + y * TILE_SIZE

            screen.blit(ground_img, (pixel_x, pixel_y))

            if tile == 1:
                draw_growing_grass(x, y, pixel_x, pixel_y, dt)
            elif tile == 2:
                draw_growing_tree(x, y, pixel_x, pixel_y, dt)

def draw_growing_grass(x, y, pixel_x, pixel_y, dt):
    # обновляем таймер роста
    current = growth_time[y][x]
    current = min(current + dt, GROWTH_DURATION)
    growth_time[y][x] = current

    progress = current / GROWTH_DURATION  # от 0.0 до 1.0

    # защита от нуля
    if progress <= 0.0:
        progress = 0.01

    target_size = int(CELL_SIZE * progress)

    # масштабируем базовый спрайт
    img = pygame.transform.smoothscale(grass_img, (target_size, target_size))

    # центрируем внутри клетки
    offset = (CELL_SIZE - target_size) // 2
    screen.blit(img, (pixel_x + offset, pixel_y + offset))

def draw_growing_tree(x, y, pixel_x, pixel_y, dt):
    # обновляем таймер роста
    current = growth_time[y][x]
    current = min(current + dt, GROWTH_DURATION)
    growth_time[y][x] = current

    progress = current / GROWTH_DURATION  # от 0.0 до 1.0

    # защита от нуля
    if progress <= 0.0:
        progress = 0.01

    target_size = int(CELL_SIZE * progress)

    # масштабируем базовый спрайт
    img = pygame.transform.smoothscale(tree_img, (target_size, target_size))

    # центрируем внутри клетки
    offset = (CELL_SIZE - target_size) // 2
    screen.blit(img, (pixel_x + offset, pixel_y + offset))


