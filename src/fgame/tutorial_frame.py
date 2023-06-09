import pygame
from ult.text_display import *
from ult.buttons import *
from ult.display import *

class Tutorial_frame():
    def __init__(self, screen, Xscreen, Yscreen):
        self.screen = screen
        self.Xscreen = Xscreen
        self.Yscreen = Yscreen
    
    def display_tutorialtext(self):
        content = ['Guess the CDI organization that the Boss Of Organization (BOO)                 is thinking about through',
                    'a series of questions',
                    '  - Each round has two randomly questions from 24 questions. Users can choose one of these two to',
                    'reveal a hint about this organization. They can ask maximum of 22 questions for each organization.',
                    '  - List of buttons:',
                    '',
                    '     : to return back to Main Menu.',
                    '',
                    '     : to return back to Question frame.',
                    '',
                    '     : to reveal one the three organizations the BOO is thinkning about.',
                    '',
                    '     : to change the organization BOO is thinking about.'
                    '',
                    '',
                    '  - Scoring: Every time you ask a quesiton, BOO will take away 20 points from you. If you answer wrong,',
                    'your score is 0 by default. Otherwise, your total score = 440 - total asked questions x 20']

        font = pygame.font.SysFont('Comicsansms', 20)

        para_y = 150
        line_spacing = 25
        for i in range(len(content)):    
            text = font.render(content[i], 1, (0,0,0))
            textRect = text.get_rect()
            if i == 0: textRect.topleft = (50, para_y)
            else: textRect.topleft = (30, para_y)
            para_y += line_spacing
            self.screen.blit(text, textRect)

            # Title
            tutorial, tutorial_Rect = text_box(
                'Impact',
                'Tutorial',
                28,
                self.Xscreen//2,
                self.Yscreen//2-210,
                (252, 165, 16)
            )
            self.screen.blit(tutorial, tutorial_Rect)
    
    def display_tutorial(self):
        fixed_textRect = pygame.Rect(30, 50, 1000, 500)
        fixed_textRect.center = (self.Xscreen//2, self.Yscreen//2)
        pygame.draw.rect(self.screen, (0,0,0), fixed_textRect, 3, 10)
        
        self.display_tutorialtext()

        # Image
        display_element(self.screen, './sprites/deco/me.png', 720, 150, 0.15)
        display_element(self.screen, './sprites/Extras/home.png', 40, 300, 0.1)
        display_element(self.screen, './sprites/Extras/arrow.png', 40, 360, 0.05, 180)
        display_element(self.screen, './sprites/Extras/answer_orginal.png', 40, 410, 0.08)
        display_element(self.screen, './sprites/Extras/restart.png', 40, 460, 0.07)