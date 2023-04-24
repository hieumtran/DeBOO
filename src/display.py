import pygame
from guess_game import *
from question_frame import *

def text_box(content, loctextX, loctextY, screen):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(content, 1, (0, 0, 0))

    # text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (loctextX*3/5, loctextY*1/2.7)
    screen.blit(text, textRect)

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
    
        text_box(f'Choose a quesion:', Xscreen, Yscreen, screen)
        display_textbox(screen, Xscreen, Yscreen)
        add_characters(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print(mouseX, mouseY)
            if event.type == pygame.QUIT:
                running = False
                
        # Draws the surface object to the screen.
        pygame.display.update()



