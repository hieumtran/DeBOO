import pygame

def text_box(font, content, size, loctextX, loctextY, color, bold=False):
    font = pygame.font.SysFont(font, size)
    if bold == True: font.bold = True
    text = font.render(content, 1, color)
    # text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (loctextX, loctextY)
    return text, textRect

def display_bubble(screen, loctextX, loctextY):
    text_bubble = pygame.image.load('./sprites/Extras/text_bubbles.png')
    # Scale the image to your needed size
    text_bubble = pygame.transform.scale_by(text_bubble, 0.2)
    screen.blit(text_bubble, (loctextX*3/5*4/6, loctextY*1/3*3/6))

def display_animationbox(screen, textRect, locX, locY, width, height):
    fixed_textRect = pygame.Rect(locX, locY, width, height)
    fixed_textRect.center = textRect.center
    pygame.draw.rect(screen, (0,0,0), fixed_textRect, 3, 10)
    return fixed_textRect
