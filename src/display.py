import pygame
# import os
# os.environ["SDL_VIDEODRIVER"]="x11"

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()
screen = pygame.display.set_mode((640, 240))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()