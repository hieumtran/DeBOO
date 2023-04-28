import pygame
from ult.text_display import *
from ult.buttons import *

class Menu_frame():
    def __init__(self, screen, Xscreen, Yscreen):
        self.screen = screen
        self.Xscreen = Xscreen
        self.Yscreen = Yscreen
    
    def add_characters(self):
        character = pygame.image.load('./sprites/character/Ask_Me.jpg')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.63)
        self.screen.blit(character, (-60, 300)) 
    
    def add_characters_2(self):
        character = pygame.image.load('./sprites/character/flip.png')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.63)
        self.screen.blit(character, (730, 300)) 
    
    def add_deco_1(self):
        character = pygame.image.load('./sprites/deco/deco_menu_1.jpg')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.8)
        character_rect = character.get_rect()
        character_rect.center = (150, 130)
        self.screen.blit(character, character_rect)
    
    def add_deco_2(self):
        character = pygame.image.load('./sprites/deco/deco_menu_2.png')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.3)
        character_rect = character.get_rect()
        character_rect.center = (800, 150)
        self.screen.blit(character, character_rect) 
       
    def display_menu(self, size, hoover_start, hoover_tutorial):
        # Start box
        if hoover_start:
            start, startRect = text_box(
                './font/Atma-Bold.ttf', 
                'START', 
                size+20, 
                self.Xscreen//2, 
                self.Yscreen//2+100, 
                (0, 0, 0), 
                custom_font=True
                # bold=True
            )
            display_animationbox(
                self.screen,
                startRect,
                30, 50, 405+20, 105+20
            )
            startRect_interact_1 = display_animationbox(
                self.screen,
                startRect,
                30, 50, 400+20, 100+20
            )
        else:
            start, startRect = text_box(
                './font/Atma-Bold.ttf', 
                'START', 
                size, 
                self.Xscreen//2, 
                self.Yscreen//2+100, 
                (0, 0, 0), 
                custom_font=True
                # bold=True
            )
            display_animationbox(
                self.screen,
                startRect,
                30, 50, 405, 105
            )
            startRect_interact_1 = display_animationbox(
                self.screen,
                startRect,
                30, 50, 400, 100
            )
        
        pygame.draw.rect(self.screen, (255,245,0), startRect_interact_1, 0, 10)
        self.screen.blit(start, startRect)

        if hoover_tutorial:
            tutorial, tutorialRect = text_box(
                './font/Atma-Bold.ttf', 
                'TUTORIAL', 
                size+20, 
                self.Xscreen//2, 
                self.Yscreen//2+250, 
                (255, 255, 255), 
                custom_font=True
                # bold=True
            )
            tutorialRect_shadow = display_animationbox(
                self.screen,
                tutorialRect,
                30, 50, 405+20, 105+20
            )
            tutorialRect_interact_1 = display_animationbox(
                self.screen,
                tutorialRect,
                30, 50, 400+20, 100+20
            )
        else:
            tutorial, tutorialRect = text_box(
                './font/Atma-Bold.ttf', 
                'TUTORIAL', 
                size, 
                self.Xscreen//2, 
                self.Yscreen//2+250, 
                (255, 255, 255), 
                custom_font=True
                # bold=True
            )
            tutorialRect_shadow = display_animationbox(
                self.screen,
                tutorialRect,
                30, 50, 405, 105
            )
            tutorialRect_interact_1 = display_animationbox(
                self.screen,
                tutorialRect,
                30, 50, 400, 100
            )

        pygame.draw.rect(self.screen, (255,245,0), tutorialRect_shadow, 3, 10)
        pygame.draw.rect(self.screen, (0,0,0), tutorialRect_interact_1, 0, 10)
        self.screen.blit(tutorial, tutorialRect)

        # Title
        deboo, debooRect = text_box(
            './font/Atma-Bold.ttf', 
            'DeBOO', 
            48+50, 
            self.Xscreen//2, 
            self.Yscreen//2-100, 
            (255,245,0), 
            custom_font=True
            # bold=True
        )
        deboo_shadow = display_animationbox(
            self.screen,
            debooRect,
            30, 50, 405, 155
        )
        deBoo_interact = display_animationbox(
            self.screen,
            debooRect,
            30, 50, 400, 150
        )
        pygame.draw.rect(self.screen, (255, 254, 0), deboo_shadow, 3, 10)
        pygame.draw.rect(self.screen, (0,0,0), deBoo_interact, 0, 10)
        self.screen.blit(deboo, debooRect)

        self.add_characters()
        self.add_characters_2()
        self.add_deco_1()
        self.add_deco_2()

        return startRect, tutorialRect


