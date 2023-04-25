import pygame
from guess_game import *
from question_frame import *
from response_frame import *
import pandas as pd
import random
import time

# Init game resolution
pygame.init()
vresolution, hresolution = pygame.display.get_desktop_sizes()[0]
Xscreen, Yscreen = vresolution*4/5, hresolution*4/5
screen = pygame.display.set_mode((Xscreen, Yscreen))

# Running condition
running = True

# Game Logic
df = pd.read_csv('./data/Q_CDI.csv')
read_question = pd.read_csv('./data/Q_ID.csv')
read_question = read_question.set_index('ID')

org = df['Organization']

question = df.columns[4:].to_list()

seed = 0
frames = [0, 0, 1, 0, ]
'''
0: Menu
1: Question
2: Thinking
3: Response
'''

fquest_frame = Q_frame(screen, Xscreen, Yscreen, 'Choose a question')
fresponse_frame = Response_frame(screen, Xscreen, Yscreen)
while running:
    # White background color
    screen.fill((255, 255, 255))

    curr_org = np.random.choice(org, size=1, replace=False)[0]
    goal = df.loc[df['Organization'] == curr_org].iloc[:, 4:]
    question = df.columns[4:].to_list()
    game_question = df.columns[4:].to_list()

    # May reshuffle the questions
    random.seed(seed)
    random.shuffle(game_question)

    curr_quest_1 = 0
    curr_quest_2 = 1

    # Question frame
    if frames[1] == 1:
        

        interact_1, interact_2 = fquest_frame.display(
            read_question.loc[game_question[curr_quest_1], :].values[0],
            read_question.loc[game_question[curr_quest_2], :].values[0]
        )

        mpos = pygame.mouse.get_pos() # Get mouse position
        if interact_1.collidepoint(mpos):
            pygame.draw.rect(screen, (255, 0, 0), interact_1, 3, 10)
        if interact_2.collidepoint(mpos):
            pygame.draw.rect(screen, (255, 0, 0), interact_2, 3, 10)
        
    # Thinking frame
    if frames[2] == 1:
        fresponse_frame.display_thinking('Hmmmm.....')
        # pygame.time.wait(2000)
        time.sleep(2)
        frames[2], frames[3] = 0, 1
        
    # Response frame
    if frames[3] == 1:
        fresponse_frame.display_response(1)
        # pygame.time.wait(2000)
        time.sleep(2)
        frames[3], frames[2] = 0, 1

    # Play action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Question frame
            if pygame.mouse.get_pressed()[0]:
                mpos = pygame.mouse.get_pos()
                if interact_1.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    # Change frame
                if interact_2.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    # Change frame
    
            
    # Draws the surface object to the screen.
    pygame.display.update()



