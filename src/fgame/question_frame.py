import pygame
from ult.text_display import *
import numpy as np


class Q_frame():
    def __init__(self, screen, loctextX, loctextY, content):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY
        self.content = content

    def add_characters(self):
        character = pygame.image.load('./sprites/character/Ask_Me.jpg')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.63)
        self.screen.blit(character, (100, 300)) 
    
    def add_characters_NMQ(self):
        character = pygame.image.load('./sprites/character/NMQ.png')
        # Scale the image to your needed size
        character = pygame.transform.scale_by(character, 0.22)
        self.screen.blit(character, (100, 300)) 
    
    def display_questionbox(self, textRect):
        fixed_textRect = pygame.Rect(30, 30, 570, 50)
        fixed_textRect.center = textRect.center
        pygame.draw.rect(self.screen, (0,0,0), fixed_textRect, 3, 10)
        return fixed_textRect

    def sample_questions(self, game_question):
        if len(game_question) > 2:
            ask_question_ID = np.random.choice(game_question, size=2, replace=False)
        assert len(ask_question_ID) == 2
        return ask_question_ID

    def display(self, question_1, question_2):
        display_bubble(self.screen, self.loctextX, self.loctextY)
        self.add_characters()  
        text_color = (0,0,0)
        # Text with bubble Display
        text_conv, textRect_conv = text_box(
            'Comicsansms',
            self.content, 
            25,
            self.loctextX*3/5, 
            self.loctextY*1/2.7,
            text_color
        )
        self.screen.blit(text_conv, textRect_conv)
        
        # Text with Rect Display
        text_1, textRect_1 = text_box(
            'Comicsansms',
            question_1,
            16,
            self.loctextX*5/7, 
            self.loctextY*2/2.7,
            text_color
        )
        self.screen.blit(text_1, textRect_1)
        textRect_interact_1 = display_animationbox(
            self.screen,
            textRect_1,
            30, 30, 570, 50
        )
        
        text_2, textRect_2 = text_box(
            'Comicsansms',
            question_2,
            16,
            self.loctextX*5/7, 
            self.loctextY*2.3/2.7,
            text_color
        )
        self.screen.blit(text_2, textRect_2)
        textRect_interact_2 = display_animationbox(
            self.screen,
            textRect_2,
            30, 30, 570, 50
        )
        return textRect_interact_1, textRect_interact_2

    def display_NMQ(self):
        display_bubble(self.screen, self.loctextX, self.loctextY)
        self.add_characters_NMQ()  
        text_color = (0,0,0)
        # Text with bubble Display
        text_conv, textRect_conv = text_box(
            'Comicsansms',
            'No more question!!!!', 
            25,
            self.loctextX*3/5, 
            self.loctextY*1/2.7,
            text_color
        )
        self.screen.blit(text_conv, textRect_conv)