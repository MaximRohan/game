# Example file showing a basic pygame "game loop"
import pygame
import settings
import os


from world import field as field_module

from actions import movement, harvest, plant

# pygame setup
pygame.init()

growth_time = field_module.growth_time
field = field_module.field

screen = settings.screen
MAP_WIDTH = settings.MAP_WIDTH
MAP_HEIGHT = settings.MAP_HEIGHT
TILE_SIZE = settings.TILE_SIZE
clock = pygame.time.Clock()
running = True

# путь к картинке
IMG_DIR = os.path.join(os.path.dirname(__file__), "img")
PLAYER_PATH = os.path.join(IMG_DIR, "player.png")

player_img = pygame.image.load(PLAYER_PATH).convert_alpha()
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))

# Если ИСХОДНИК смотрит ВНИЗ:
img_down = player_img
img_up = pygame.transform.rotate(player_img, 180)
img_left = pygame.transform.rotate(player_img, -90)
img_right = pygame.transform.rotate(player_img, 90)

FIELD_OFFSET_X = 5
FIELD_OFFSET_Y = 5

direction = "up"
player_x = 0
player_y = 9

while running:
    dt = clock.tick(60) / 1000
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = "up"
                player_x, player_y = movement.try_move(field, player_x, player_y, 0, -1)
            elif event.key == pygame.K_s:
                direction = "down"
                player_x, player_y = movement.try_move(field, player_x, player_y, 0, 1)
            elif event.key == pygame.K_a:
                direction = "left"
                player_x, player_y = movement.try_move(field, player_x, player_y, -1, 0)
            elif event.key == pygame.K_d:
                direction = "right"
                player_x, player_y = movement.try_move(field, player_x, player_y, 1, 0)
            elif event.key == pygame.K_SPACE:
                harvest.harvest(field, player_x, player_y, growth_time)
            elif event.key == pygame.K_1:
                plant.plant_grass(field, player_x, player_y)
            elif event.key == pygame.K_2:
                plant.plant_tree(field, player_x, player_y)


    field_module.field_draw(dt)

    if direction == "up":
        current_img = img_up
    elif direction == "down":
        current_img = img_down
    elif direction == "left":
        current_img = img_left
    elif direction == "right":
        current_img = img_right

    px = FIELD_OFFSET_X + player_x * TILE_SIZE
    py = FIELD_OFFSET_Y + player_y * TILE_SIZE
    screen.blit(current_img, (px, py))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()