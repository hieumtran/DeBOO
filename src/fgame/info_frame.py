import pygame

class Info_frame():
    def __init__(self, screen, loctextX, loctextY):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY
    
    def drawText(self, text, color, rect, font, aa=False, bkg=None):
        # rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i > len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            self.screen.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

    def display_info(self, df, curr_org):
        curr_org = "Minority Association of Pre-Medication Students"
        display_org = df.loc[df['Organization'] == curr_org, :]

        fixed_textRect = pygame.Rect(30, 50, 1000, 500)
        fixed_textRect.center = (self.loctextX//2, self.loctextY//2)
        pygame.draw.rect(self.screen, (0,0,0), fixed_textRect, 3, 10)

        # Display Text
        content = display_org.loc[:, 'Description'].values[0]
        content = content.split('\n')

        font = pygame.font.SysFont('Comicsansms', 20)

        para_y = 150
        line_spacing = 25
        for i in range(len(content)):    
            text = font.render(content[i], 1, (0,0,0))
            # text surface object
            textRect = text.get_rect()
            # set the center of the rectangular object.
            if i == 0:
                textRect.topleft = (50, para_y)
            else:
                textRect.topleft = (30, para_y)
            para_y += line_spacing
            self.screen.blit(text, textRect)
        

        

        