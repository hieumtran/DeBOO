import pygame
from text_display import *
import numpy as np

class Response_frame():
    def __init__(self, screen, loctextX, loctextY):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY

    def add_character_thinking(self):
        character = pygame.image.load('./sprites/character/Thinking.png')
        character = pygame.transform.scale_by(character, 0.4)
        self.screen.blit(character, (100, 250)) 

    def add_character(self, file, scale, loc):
        character = pygame.image.load(file)
        character = pygame.transform.scale_by(character, scale)
        self.screen.blit(character, loc) 

    def display_thinking(self, content):
        display_bubble(self.screen, self.loctextX, self.loctextY)
        self.add_character_thinking()

        text, textRect = text_box(
            content, 
            25,
            self.loctextX*3/5, 
            self.loctextY*1/2.7
        )
        self.screen.blit(text, textRect) 

    def display_response(self, value, content_ID):
        path = './sprites/character/'
        
        yes_content = [
            'Yes, absolutely', 
            'Yup!', 
            'Yes, good question!',
            'I think so', 
            'I guess so'
        ]
        no_content = [
            'No, nahhh!', 
            'Nope!', 
            'No, try another one!',
            "I don't think so", 
            'I guess not'
        ]

        # No
        if value == 0:
            content = no_content[content_ID]
            if content_ID == 0: self.add_character(f'{path}No_0.png', 0.2, (100, 250)) # Done
            if content_ID == 1: self.add_character(f'{path}No_1.png', 0.18, (100, 290)) # Done
            if content_ID == 2: self.add_character(f'{path}No_2.png', 0.7, (100, 290)) # Done
            if content_ID == 3: self.add_character(f'{path}No_3.png', 0.45, (40, 280)) # Done
            if content_ID == 4: self.add_character(f'{path}No_4.jpg', 0.46, (100, 340)) # Done
        
        # Yes
        if value == 1:
            content = yes_content[content_ID]
            if content_ID == 0: self.add_character(f'{path}Yes_0.png', 0.74, (90, 280)) # Done
            if content_ID == 1: self.add_character(f'{path}Yes_1.png', 0.8, (90, 280)) # Done
            if content_ID == 2: self.add_character(f'{path}Yes_2.jpg', 0.6, (40, 250)) # Done
            if content_ID == 3: self.add_character(f'{path}Yes_3.png', 0.8, (70, 250)) # Done
            if content_ID == 4: self.add_character(f'{path}Yes_4.png', 0.6, (100, 300)) # Done

        display_bubble(self.screen, self.loctextX, self.loctextY)
        text, textRect = text_box(
            content, 
            25,
            self.loctextX*3/5, 
            self.loctextY*1/2.7
        )
        self.screen.blit(text, textRect) 

