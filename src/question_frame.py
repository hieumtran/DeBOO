import pygame
from text_display import *


class Q_frame():
    def __init__(self, screen, loctextX, loctextY, content):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY
        self.content = content

    def display_textbox(self):
        text_bubble = pygame.image.load('./sprites/text_bubbles.png')
        # Scale the image to your needed size
        text_bubble = pygame.transform.scale_by(text_bubble, 0.2)
        self.screen.blit(text_bubble, (self.loctextX*3/5*4/6, self.loctextY*1/3*3/6))

    def add_characters(self):
        character = pygame.image.load('./sprites/character/Ask_Me_2-removebg-preview.png')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.65)
        self.screen.blit(character, (100, 300)) 
    
    def display_questionbox(self, text, textRect):
        fixed_textRect = pygame.Rect(30, 30, 570, 50)
        fixed_textRect.center = textRect.center
        pygame.draw.rect(self.screen, (0,0,0), fixed_textRect, 3, 10)

        

    def display(self, question_1, question_2):
        self.display_textbox()
        self.add_characters()  

        # Text with bubble Display
        text_conv, textRect_conv = text_box(
            f'Choose a quesion:', 
            25,
            self.loctextX*3/5, 
            self.loctextY*1/2.7
        )
        self.screen.blit(text_conv, textRect_conv)
        
        # Text with Rect Display
        text_1, textRect_1 = text_box(
            question_1,
            16,
            self.loctextX*5/7, 
            self.loctextY*2/2.7
        )
        self.screen.blit(text_1, textRect_1)
        self.display_questionbox(text_1, textRect_1)

        text_2, textRect_2 = text_box(
            question_2,
            16,
            self.loctextX*5/7, 
            self.loctextY*2.3/2.7
        )
        self.screen.blit(text_2, textRect_2)
        self.display_questionbox(text_2, textRect_2)