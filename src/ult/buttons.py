import pygame

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def display_arrow(Xscreen, Yscreen):
    arrow = pygame.image.load('./sprites/Extras/arrow.png').convert_alpha()
    arrow = pygame.transform.rotate(arrow, 180)
    arrow = pygame.transform.scale_by(arrow, 0.07)
    arrow_rect = arrow.get_rect()
    
    arrow_rect.center = (Xscreen//2-470, Yscreen//2-280)
    return arrow, arrow_rect