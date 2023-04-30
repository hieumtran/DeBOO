import pygame


def display_element(
        screen,
        filename,
        locX,
        locY,
        scale=None,
        rotation=None
    ):
    '''Render sprites on pygame window'''
    # Load image
    image = pygame.image.load(filename)
    if scale != None: image = pygame.transform.scale_by(image, scale)
    if rotation != None: image = pygame.transform.rotate(image, rotation)
    image_rect = image.get_rect()
    image_rect.center = (locX, locY)
    screen.blit(image, image_rect)

    return image, image_rect


def display_text(
        font, 
        content,
        size, 
        locX, 
        locY, 
        color, 
        bold=None, 
        custom_font=None
    ):
    '''Render text on pygame window'''
    if custom_font: font = pygame.font.Font(font, size)
    else: font = pygame.font.SysFont(font, size)
    if bold: font.bold = bold
    text = font.render(content, 1, color)
    textRect = text.get_rect()
    textRect.center = (locX, locY)
    return text, textRect


def display_textbox(
        screen, 
        textRect, 
        locX, 
        locY, 
        width, 
        height
    ):
    '''Wrap box for text display'''
    fixed_textRect = pygame.Rect(locX, locY, width, height)
    fixed_textRect.center = textRect.center
    pygame.draw.rect(screen, (0,0,0), fixed_textRect, 3, 10)
    return fixed_textRect