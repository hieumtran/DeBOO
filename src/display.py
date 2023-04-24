import pygame
from guess_game import *
from question_frame import *
import pandas as pd

if __name__ == "__main__":
    # Init screen
    pygame.init()
    vresolution, hresolution = pygame.display.get_desktop_sizes()[0]
    Xscreen, Yscreen = vresolution*4/5, hresolution*4/5
    screen = pygame.display.set_mode((Xscreen, Yscreen))

    running = True
    while running:
        # completely fill the surface object
        # with white color
        white = (255, 255, 255)
        screen.fill(white)

        # Initializing Color
        # color = (48, 141, 70)
        
        # Drawing Rectangle
        # pygame.draw.rect(screen, color, pygame.Rect(Xscreen*5/7, Yscreen*2/2.7, 60, 60),  2, 3)
    
        screen_frame = Q_frame(screen, Xscreen, Yscreen, 'Choose a question')
        screen_frame.display('Did this organization hold a Baazar?',
                              'Does this organization primarily promote Asian activities and cultures?')

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                
        # Draws the surface object to the screen.
        pygame.display.update()



