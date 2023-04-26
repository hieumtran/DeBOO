import pygame

def text_box(font, content, size, loctextX, loctextY, color):
    # font = pygame.font.Font('freesansbold.ttf', size)
    font = pygame.font.SysFont(font, size)
    text = font.render(content, 1, color)

    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (loctextX, loctextY)
    return text, textRect

def display_bubble(screen, loctextX, loctextY):
    text_bubble = pygame.image.load('./sprites/text_bubbles.png')
    # Scale the image to your needed size
    text_bubble = pygame.transform.scale_by(text_bubble, 0.2)
    screen.blit(text_bubble, (loctextX*3/5*4/6, loctextY*1/3*3/6))
    