import pygame
# from ult.text_display import *
from ult.buttons import *
from ult.display import *

class Menu_frame():
    def __init__(self, screen, Xscreen, Yscreen):
        self.screen = screen
        self.Xscreen = Xscreen
        self.Yscreen = Yscreen

    def display_deco(self):
        display_element(
            self.screen,
            './sprites/character/Ask_Me.jpg',
            110, 
            500,
            0.63
        )
        display_element(
            self.screen,
            './sprites/character/flip.png',
            910,
            500,
            0.63
        )
        display_element(
            self.screen,
            './sprites/deco/deco_menu_1.jpg',
            150, 
            130,
            0.8
        )
        display_element(
            self.screen,
            './sprites/deco/deco_menu_2.png',
            800, 
            150,
            0.3
        )

    def display_menu(self, size, hoover_start, hoover_tutorial):
        # Title
        deboo, debooRect = display_text(
            './font/Atma-Bold.ttf', 
            'DeBOO', 
            48+50, 
            self.Xscreen//2, 
            self.Yscreen//2-100, 
            (255,245,0), 
            custom_font=True
            # bold=True
        )
        deboo_shadow = display_textbox(
            self.screen,
            debooRect,
            30, 50, 405, 155
        )
        deBoo_interact = display_textbox(
            self.screen,
            debooRect,
            30, 50, 400, 150
        )

        # Start button
        if hoover_start:
            start, startRect = display_text(
                './font/Atma-Bold.ttf', 
                'START', 
                size+20, 
                self.Xscreen//2, 
                self.Yscreen//2+100, 
                (0, 0, 0), 
                custom_font=True
                # bold=True
            )
            display_textbox(
                self.screen,
                startRect,
                30, 50, 405+20, 105+20
            )
            startRect_interact_1 = display_textbox(
                self.screen,
                startRect,
                30, 50, 400+20, 100+20
            )
        else:
            start, startRect = display_text(
                './font/Atma-Bold.ttf', 
                'START', 
                size, 
                self.Xscreen//2, 
                self.Yscreen//2+100, 
                (0, 0, 0), 
                custom_font=True
                # bold=True
            )
            display_textbox(
                self.screen,
                startRect,
                30, 50, 405, 105
            )
            startRect_interact_1 = display_textbox(
                self.screen,
                startRect,
                30, 50, 400, 100
            )

        # Tutorial button
        if hoover_tutorial:
            tutorial, tutorialRect = display_text(
                './font/Atma-Bold.ttf', 
                'TUTORIAL', 
                size+20, 
                self.Xscreen//2, 
                self.Yscreen//2+250, 
                (255, 255, 255), 
                custom_font=True
                # bold=True
            )
            tutorialRect_shadow = display_textbox(
                self.screen,
                tutorialRect,
                30, 50, 405+20, 105+20
            )
            tutorialRect_interact_1 = display_textbox(
                self.screen,
                tutorialRect,
                30, 50, 400+20, 100+20
            )
        else:
            tutorial, tutorialRect = display_text(
                './font/Atma-Bold.ttf', 
                'TUTORIAL', 
                size, 
                self.Xscreen//2, 
                self.Yscreen//2+250, 
                (255, 255, 255), 
                custom_font=True
                # bold=True
            )
            tutorialRect_shadow = display_textbox(
                self.screen,
                tutorialRect,
                30, 50, 405, 105
            )
            tutorialRect_interact_1 = display_textbox(
                self.screen,
                tutorialRect,
                30, 50, 400, 100
            )
        
        pygame.draw.rect(self.screen, (255, 254, 0), deboo_shadow, 3, 10)
        pygame.draw.rect(self.screen, (0,0,0), deBoo_interact, 0, 10)
        pygame.draw.rect(self.screen, (255,245,0), startRect_interact_1, 0, 10)
        pygame.draw.rect(self.screen, (255,245,0), tutorialRect_shadow, 3, 10)
        pygame.draw.rect(self.screen, (0,0,0), tutorialRect_interact_1, 0, 10)

        self.screen.blit(deboo, debooRect)
        self.screen.blit(start, startRect)
        self.screen.blit(tutorial, tutorialRect)

        self.display_deco()

        return startRect, tutorialRect


