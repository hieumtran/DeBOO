import pygame
from ult.text_display import *

class Info_frame():
    def __init__(self, screen, loctextX, loctextY):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY

    def blit_icon(self, filename, scale, alpha, locX, locY):
        icon = pygame.image.load(f"./sprites/icon/{filename}")
        icon.set_alpha(alpha)
        icon = pygame.transform.scale_by(icon, scale)
        icon_rect = icon.get_rect()
        icon_rect.center = (locX, locY)
        self.screen.blit(icon, icon_rect) 

    def display_info(self, df, curr_org):
        display_org = df.loc[df['Organization'] == curr_org, :]

        # Display icon
        self.fdisplay_icon(curr_org, display_org)
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
        
        OrgTitle, OrgTitle_Rect = text_box(
            'Impact',
            curr_org,
            28,
            self.loctextX//2,
            self.loctextY//2-210,
            (252, 165, 16)
        )
        self.screen.blit(OrgTitle, OrgTitle_Rect)

    def fdisplay_icon(self, curr_org, display_org):
        # Display background image
        if curr_org == "African Students' Association": 
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2
            )
        if curr_org == "Association of African-American Students": 
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.5, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "Caribbean Student Association":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.5, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "Committee for Latinx Concerns":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.1, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "Computing Opportunities for Students of Color":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "DePauw China Connection":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "DePauw International Student Association":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+100
            )
        if curr_org == "Elite Precizion":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.1, 125,
                self.loctextX//2, self.loctextY//2
            )     
        if curr_org == "Exalt! Gospel Choir":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2
            )     
        if curr_org == "Feminista!":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+70
            )     
        if curr_org == "House of Opulence":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.5, 255,
                self.loctextX//2, self.loctextY//2+100
            )  
        if curr_org == "Japanese Club":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+100
            )    
        if curr_org == "La Fuerza Latina Latin Dance Group":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.2, 125,
                self.loctextX//2, self.loctextY//2
            )    
        if curr_org == "Native American & Indigenous People Association":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.4, 255,
                self.loctextX//2, self.loctextY//2+100
            )    
        if curr_org == "Students of Color in STEM":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+125
            )    
        if curr_org == "South Asian Student Society":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.28, 255,
                self.loctextX//2, self.loctextY//2+100
            )   
        if curr_org == "The Brotherhood":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.5, 125,
                self.loctextX//2, self.loctextY//2
            )   
        if curr_org == "The HEAT":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.5, 255,
                self.loctextX//2, self.loctextY//2+100
            ) 
        if curr_org == "Vietnamese Student Association":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.3, 255,
                self.loctextX//2, self.loctextY//2+50
            ) 
        if curr_org == "Association of Asian, Pacific Islander, and Desi American":
            pass     
        if curr_org == "Ladies and Allies for Cross-Cultural Education":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                1, 255,
                self.loctextX//2, self.loctextY//2+50
            ) 
        if curr_org == "Minority Association of Pre-Medication Students":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                1, 255,
                self.loctextX//2, self.loctextY//2+100
            ) 
        if curr_org == "The X-Cell Dance Team":
            self.blit_icon(
                display_org.loc[:, 'Image'].values[0], 
                0.25, 255,
                self.loctextX//2, self.loctextY//2+100
            ) 