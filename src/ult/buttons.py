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
    
    arrow_rect.center = (Xscreen//2-470, Yscreen//2+280)
    return arrow, arrow_rect

def display_home(Xscreen, Yscreen):
    home = pygame.image.load('./sprites/Extras/Home.png').convert_alpha()
    home = pygame.transform.scale_by(home, 0.15)
    home_rect = home.get_rect()

    home_rect.center = (Xscreen, Yscreen)
    return home, home_rect

def display_restart(Xscreen, Yscreen):
    home = pygame.image.load('./sprites/Extras/restart.png').convert_alpha()
    home = pygame.transform.scale_by(home, 0.15)
    home_rect = home.get_rect()

    home_rect.center = (Xscreen, Yscreen)
    return home, home_rect

def add_deco(screen, file, scale, Xscreen, Yscreen):
    image = pygame.image.load(file)
    # Scale the image to your needed size
    image = pygame.transform.scale_by(image, scale)
    image_rect = image.get_rect()
    image_rect.center = (Xscreen, Yscreen)
    screen.blit(image, image_rect)