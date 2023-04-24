import pygame

def text_box(content, size, loctextX, loctextY):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(content, 1, (0, 0, 0))

    # text surface object
    textRect = text.get_rect()
    # print(vars(textRect))
    # set the center of the rectangular object.
    textRect.center = (loctextX, loctextY)
    return text, textRect

def text_box_question(content, size, loctextX, loctextY):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(content, 1, (0, 0, 0))

    # text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (loctextX, loctextY)
    return text, textRect
    
    