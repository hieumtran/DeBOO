import pygame
import time
game_font = pygame.font.get_fonts()

# import pygame module in this program
import pygame
 
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
# assigning values to X and Y variable
X = 400
Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
# font = pygame.font.Font('arial', 32)


# infinite loop
i = 0
while True:
 
    # completely fill the surface object
    # with white color
    display_surface.fill(white)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.

    font = pygame.font.SysFont(game_font[i], 32)
 
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(game_font[i], True, green, blue)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)
    display_surface.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
        if pygame.mouse.get_pressed()[0]:
            i += 1
 
        # Draws the surface object to the screen.
        pygame.display.update()
