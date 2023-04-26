import pygame
import numpy as np
import random
from ult.text_display import *

class Answer_frame():
    def __init__(self, screen, loctextX, loctextY):
        self.screen = screen
        self.loctextX = loctextX
        self.loctextY = loctextY
    
    def display_answerbox(self, textRect):
        fixed_textRect = pygame.Rect(30, 50, 1000, 100)
        fixed_textRect.center = textRect.center
        pygame.draw.rect(self.screen, (0,0,0), fixed_textRect, 3, 10)
        return fixed_textRect

    def display_answer(self, answer_list):
        text_color = (0,0,0)
        text_1, textRect_1 = text_box(
            'Comicsansms',
            answer_list[0], 
            32,
            self.loctextX//2, 
            self.loctextY//2-150,
            text_color
        )
        self.screen.blit(text_1, textRect_1)
        textRect_interact_1 = self.display_answerbox(textRect_1)
        
        text_2, textRect_2 = text_box(
            'Comicsansms',
            answer_list[1], 
            32,
            self.loctextX//2, 
            self.loctextY//2,
            text_color
        )
        self.screen.blit(text_2, textRect_2)
        textRect_interact_2 = self.display_answerbox(textRect_2)

        text_3, textRect_3 = text_box(
            'Comicsansms',
            answer_list[2], 
            32,
            self.loctextX//2, 
            self.loctextY//2+150,
            text_color
        )
        self.screen.blit(text_3, textRect_3)
        textRect_interact_3 = self.display_answerbox(textRect_3)
        return textRect_interact_1, textRect_interact_2, textRect_interact_3

    def discriminator(self, correct_index, interact_1, interact_2, interact_3):
        checkmark = pygame.image.load('./sprites/Extras/checkmark.png')
        checkmark = pygame.transform.scale_by(checkmark, 0.15)
        x_mark = pygame.image.load('./sprites/Extras/Red_X.svg')
        x_mark = pygame.transform.scale_by(x_mark, 0.9)

        if correct_index == 0:
            self.screen.blit(checkmark, (interact_1.topleft[0]+5, interact_1.topleft[1]+10))  
            self.screen.blit(checkmark, (interact_1.topright[0]-95, interact_1.topright[1]+10))  
            self.screen.blit(x_mark, (interact_2.topleft[0]+5, interact_2.topleft[1]+5))  
            self.screen.blit(x_mark, (interact_2.topright[0]-95, interact_2.topright[1]+5))   
            self.screen.blit(x_mark, (interact_3.topleft[0]+5, interact_3.topleft[1]+5))  
            self.screen.blit(x_mark, (interact_3.topright[0]-95, interact_3.topright[1]+5))   
        if correct_index == 1:
            self.screen.blit(x_mark, (interact_1.topleft[0]+5, interact_1.topleft[1]+10))  
            self.screen.blit(x_mark, (interact_1.topright[0]-95, interact_1.topright[1]+10))  
            self.screen.blit(checkmark, (interact_2.topleft[0]+5, interact_2.topleft[1]+5))  
            self.screen.blit(checkmark, (interact_2.topright[0]-95, interact_2.topright[1]+5))   
            self.screen.blit(x_mark, (interact_3.topleft[0]+5, interact_3.topleft[1]+5))  
            self.screen.blit(x_mark, (interact_3.topright[0]-95, interact_3.topright[1]+5))    
        if correct_index == 2:
            self.screen.blit(x_mark, (interact_1.topleft[0]+5, interact_1.topleft[1]+10))  
            self.screen.blit(x_mark, (interact_1.topright[0]-95, interact_1.topright[1]+10))  
            self.screen.blit(x_mark, (interact_2.topleft[0]+5, interact_2.topleft[1]+5))  
            self.screen.blit(x_mark, (interact_2.topright[0]-95, interact_2.topright[1]+5))   
            self.screen.blit(checkmark, (interact_3.topleft[0]+5, interact_3.topleft[1]+5))  
            self.screen.blit(checkmark, (interact_3.topright[0]-95, interact_3.topright[1]+5))    
        
