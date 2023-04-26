import pygame
import pandas as pd
import random

from guess_game import *
from fgame.question_frame import *
from fgame.response_frame import *
from fgame.answer_frame import *

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



seed = 0
frames = [0, 1, 0, 0, 0, 0]
'''
0: Menu
1: Question
2: Thinking
3: Response
4: Answer
5: Info
'''

fquest_frame = Q_frame(screen, Xscreen, Yscreen, 'Choose a question')
fresponse_frame = Response_frame(screen, Xscreen, Yscreen)
fanswer_frame = Answer_frame(screen, Xscreen, Yscreen)

frame_cnt_thinking = 50
frame_cnt_response = 50
frame_cnt_answer = 500

shuffle_question = True
shuffle_response = True
init_params = True
del_question = False
answer_click_state = False

interact_1, interact_2, interact_3 = None, None, None
num_quest = 0

while running:
    # White background color
    screen.fill((255, 255, 255))

    if init_params == True:
        # Init Org choice and answer
        org = df['Organization'].to_list()
        curr_org = np.random.choice(org, size=1, replace=False)[0]
        org.remove(curr_org)
        other_choice = np.random.choice(org, size=2, replace=False)
        answer_list = [curr_org, other_choice[0], other_choice[1]]
        random.shuffle(answer_list) 
        correct_index = answer_list.index(curr_org)

        # Goal
        goal = df.loc[df['Organization'] == curr_org].iloc[:, 4:]
        
        # Question
        question = df.columns[4:].to_list()
        game_question = df.columns[4:].to_list()
        init_params = False
        
    # May reshuffle the questions
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
        atext, atextRect = text_box(
            'ALGERIAN',
            'ANSWER',
            48,
            Xscreen*6.2/7,
            Yscreen/15,
            (0, 0, 0)
        )
        screen.blit(atext, atextRect)
        # Colorful Animation
        mpos = pygame.mouse.get_pos()
        if interact_1.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_1, 3, 10)
        if interact_2.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_2, 3, 10)
        if atextRect.collidepoint(mpos):
            font = pygame.font.SysFont('ALGERIAN', size=48)
            atext = font.render('ANSWER', 1, (239, 62, 91))
            screen.blit(atext, atextRect)
            
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
    
    # Answer frame
    if frames[4] == 1:
        interact_1, interact_2, interact_3 = fanswer_frame.display_answer(answer_list)
        atext, atextRect = text_box(
            'ALGERIAN',
            'Choose an answer below',
            48,
            Xscreen//2+30,
            Yscreen//2-250,
            (0, 0, 0)
        )
        screen.blit(atext, atextRect)
        mpos = pygame.mouse.get_pos()
        if interact_1.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_1, 3, 10)
        if interact_2.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_2, 3, 10)
        if interact_3.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_3, 3, 10)

        if answer_click_state:
            fanswer_frame.discriminator(correct_index, interact_1, interact_2, interact_3)
            print(curr_org)
            frame_cnt_answer -= 1
            if frame_cnt_answer < 0:
                frame_cnt_answer = 500
                answer_click_state = False

                
    # Play action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Question frame
            if pygame.mouse.get_pressed()[0] and (interact_1 != None) \
                and (interact_2 != None) and (frames[1] == 1):
                mpos = pygame.mouse.get_pos()
                if interact_1.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    value = goal.loc[:, game_question[curr_quest_1]].values[0]
                    game_question.remove(game_question[curr_quest_1])
                    shuffle_question = True
                    del_question = True
                    num_question += 1

                if interact_2.collidepoint(mpos):
                    frames[1], frames[2] = 0, 1
                    value = goal.loc[:, game_question[curr_quest_2]].values[0]
                    game_question.remove(game_question[curr_quest_2])
                    shuffle_question = True
                    del_question = True
                    num_question += 1
                    
                if atextRect.collidepoint(mpos):
                    del_question = True
                    frames[4], frames[1] = 1, 0
                
                if del_question:
                    interact_1 = None
                    interact_2 = None
                    del_question = False

            # Answer frame
            if pygame.mouse.get_pressed()[0] and (interact_1 != None) \
                and (interact_2 != None) and (interact_3 != None) and (frames[4] == 1):
                mpos = pygame.mouse.get_pos()
                answer_click_state = True

    # print(curr_org)        
    # Draws the surface object to the screen.
    pygame.display.update()



