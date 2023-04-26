import pygame
from guess_game import *
from fgame.question_frame import *
from fgame.response_frame import *
import pandas as pd
import random
import time

def waitFor(waitTime): # waitTime in milliseconds
    screenCopy = screen.copy()
    waitCount = 0
    while waitCount < waitTime:
        dt = clock.tick(60) # 60 is your FPS here
        waitCount += dt
        pygame.event.pump() # Tells pygame to handle it's event, instead of pygame.event.get()
        screen.blit(screenCopy, (0,0))
        pygame.display.flip()

clock = pygame.time.Clock()

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
frames = [0, 1, 0, 0, ]
'''
0: Menu
1: Question
2: Thinking
3: Response
'''

fquest_frame = Q_frame(screen, Xscreen, Yscreen, 'Choose a question')
fresponse_frame = Response_frame(screen, Xscreen, Yscreen)
frame_cnt_thinking = 50
frame_cnt_response = 50

shuffle_question = True
shuffle_response = True
init_params = True
del_question = False

while running:
    # White background color
    screen.fill((255, 255, 255))

    if init_params == True:
        curr_org = np.random.choice(org, size=1, replace=False)[0]
        goal = df.loc[df['Organization'] == curr_org].iloc[:, 4:]
        question = df.columns[4:].to_list()
        game_question = df.columns[4:].to_list()
        init_params = False

    # May reshuffle the questions
    # random.seed(seed)
    # np.random.seed(seed)
    if shuffle_question == True:
        random.shuffle(game_question)
        shuffle_question = False

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
        frame_cnt_thinking -= 1
        if frame_cnt_thinking < 0:
            screen.fill((255, 255, 255))
            frames[2], frames[3] = 0, 1
            frame_cnt_thinking = 75

    # Response frame
    if frames[3] == 1:
        if shuffle_response == True: 
            content_ID = np.random.randint(5, size=1)[0]
            shuffle_response = False
        fresponse_frame.display_response(value, content_ID)
        frame_cnt_response -= 1
        if frame_cnt_response < 0:
            screen.fill((255, 255, 255))
            frames[3], frames[1] = 0, 1
            frame_cnt_response = 75
            shuffle_response = True
        
    # Play action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Question frame
            if pygame.mouse.get_pressed()[0] and interact_1 != None and interact_2 != None:
                mpos = pygame.mouse.get_pos()
                if interact_1.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    value = goal.loc[:, game_question[curr_quest_1]].values[0]
                    game_question.remove(game_question[curr_quest_1])
                    shuffle_question = True
                    del_question = True

                if interact_2.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    value = goal.loc[:, game_question[curr_quest_2]].values[0]
                    game_question.remove(game_question[curr_quest_2])
                    shuffle_question = True
                    del_question = True
                
                if del_question:
                    interact_1 = None
                    interact_2 = None
                    del_question = False

    # print(curr_org)        
    # Draws the surface object to the screen.
    pygame.display.update()



