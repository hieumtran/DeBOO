import pygame
import pandas as pd
import random

from guess_game import *
from fgame.question_frame import *
from fgame.response_frame import *
from fgame.answer_frame import *
from fgame.info_frame import *
from ult.buttons import *

# Init game resolution
pygame.init()
vresolution, hresolution = pygame.display.get_desktop_sizes()[0]
# Xscreen, Yscreen = vresolution*4/5, hresolution*4/5
Xscreen, Yscreen = 1024.0, 640.0
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
finfo_frame = Info_frame(screen, Xscreen, Yscreen)

frame_cnt_thinking = 50
frame_cnt_response = 50
frame_cnt_answer = 300

frame_cnt_random = 30

shuffle_question = True
shuffle_response = True
init_params = True
init_random = True
del_question = False
answer_click_state = False
reset_arrow = False

interact_1, interact_2, interact_3 = None, None, None
arrow, arrow_rect = None, None

while running:
    # White background color
    screen.fill((255, 255, 255))

    # if frames[1] == 1 or frames[2] == 1 or frames[3] == 1:
    #     character = pygame.image.load('./sprites/character/random.png')
    #     character = pygame.transform.scale_by(character, 0.1)
    #     if init_random:
    #         xrandom = random.randint(0, Xscreen)
    #         yrandom = random.randint(0, Yscreen)
    #         init_random = False
    #     screen.blit(character, (xrandom, yrandom)) 
    #     frame_cnt_random -= 1
    #     if frame_cnt_random < 0:
    #         init_random = True
    #         frame_cnt_random = 30
        
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

    # Question frame
    if frames[1] == 1:
        if len(game_question) > 2:
            interact_1, interact_2 = fquest_frame.display(
                read_question.loc[game_question[0], :].values[0],
                read_question.loc[game_question[1], :].values[0]
            )
        else:
            fquest_frame.display_NMQ()

        # atext, atextRect = text_box(
        #     'ALGERIAN',
        #     'ANSWER',
        #     48,
        #     Xscreen*6.2/7,
        #     Yscreen/15,
        #     (0, 0, 0)
        # )
        # screen.blit(atext, atextRect)
        
        
        
        # Colorful Animation
        mpos = pygame.mouse.get_pos()
        
        arrow, arrow_rect = display_arrow(Xscreen, Yscreen)
        screen.blit(arrow, arrow_rect)
        home, home_rect = display_home(Xscreen, Yscreen)
        screen.blit(home, home_rect)
        answer_box, answer_box_rect = display_checkbox(
            screen,
            './sprites/Extras/answer_orginal.png',
            Xscreen//2+450, 50
        )
        if arrow_rect.collidepoint(mpos):
            fill(arrow, pygame.Color(255, 0, 0))
            screen.blit(arrow, arrow_rect)
        if home_rect.collidepoint(mpos):
            fill(home, pygame.Color(255, 0, 0))
            screen.blit(home, home_rect)
        if (interact_1 != None) and (interact_2 != None):
            if interact_1.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_1, 3, 10)
            if interact_2.collidepoint(mpos): pygame.draw.rect(screen, (239, 62, 91), interact_2, 3, 10)
        if answer_box_rect.collidepoint(mpos):
            answer_box, answer_box_rect = display_checkbox(            
            screen,
            './sprites/Extras/answer.png',
            Xscreen//2+450, 50
        )
        # if atextRect.collidepoint(mpos):
        #     font = pygame.font.SysFont('ALGERIAN', size=48)
        #     atext = font.render('ANSWER', 1, (239, 62, 91))
        #     screen.blit(atext, atextRect)
            
    # Thinking frame
    if frames[2] == 1:
        fresponse_frame.display_thinking('Hmmmm.....')
        frame_cnt_thinking -= 1
        if frame_cnt_thinking < 0:
            screen.fill((255, 255, 255))
            frames[2], frames[3] = 0, 1
            frame_cnt_thinking = random.randint(30, 50)

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
            frame_cnt_response = 100
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
        if answer_click_state != True: 
            arrow, arrow_rect = display_arrow(Xscreen, Yscreen)
            screen.blit(arrow, arrow_rect)
            if arrow_rect.collidepoint(mpos):
                fill(arrow, pygame.Color(255, 0, 0))
                screen.blit(arrow, arrow_rect)
        if interact_1.collidepoint(mpos): pygame.draw.rect(screen, (0, 0, 255), interact_1, 3, 10)
        if interact_2.collidepoint(mpos): pygame.draw.rect(screen, (0, 0, 255), interact_2, 3, 10)
        if interact_3.collidepoint(mpos): pygame.draw.rect(screen, (0, 0, 255), interact_3, 3, 10)

        if answer_click_state:
            fanswer_frame.discriminator(correct_index, interact_1, interact_2, interact_3)
            frame_cnt_answer -= 1
            if frame_cnt_answer < 0:
                frame_cnt_answer = 200
                answer_click_state = False
                screen.fill((255, 255, 255))
                frames[4], frames[5] = 0, 1
    
    # Information frame
    if frames[5] == 1:
        finfo_frame.display_info(df, curr_org)
        mpos = pygame.mouse.get_pos()
        if answer_click_state != True: 
            arrow, arrow_rect = display_arrow(Xscreen, Yscreen)
            screen.blit(arrow, arrow_rect)
            if arrow_rect.collidepoint(mpos):
                fill(arrow, pygame.Color(255, 0, 0))
                screen.blit(arrow, arrow_rect)
            
            home, home_rect = display_home(Xscreen, Yscreen)
            screen.blit(home, home_rect)
            if home_rect.collidepoint(mpos):
                fill(home, pygame.Color(255, 0, 0))
                screen.blit(home, home_rect)
                
    # Play action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: 
                # Question frame
                if (frames[1] == 1):
                    if (interact_1 != None) and (interact_2 != None):
                        mpos = pygame.mouse.get_pos()
                        if interact_1.collidepoint(mpos):
                            frames[1], frames[2] = 0, 1
                            value = goal.loc[:, game_question[0]].values[0]
                            game_question.remove(game_question[0])
                            shuffle_question = True
                            del_question = True

                        if interact_2.collidepoint(mpos):
                            frames[1], frames[2] = 0, 1
                            value = goal.loc[:, game_question[1]].values[0]
                            game_question.remove(game_question[1])
                            shuffle_question = True
                            del_question = True

                    if answer_box_rect != None:   
                        if answer_box_rect.collidepoint(mpos):
                            del_question = True
                            frames[4], frames[1] = 1, 0
                                                
                # Answer frame
                if (frames[4] == 1):
                    if (interact_1 != None) and (interact_2 != None) and (interact_3 != None):
                        mpos = pygame.mouse.get_pos()
                        if interact_1.collidepoint(mpos) or interact_2.collidepoint(mpos) \
                            or interact_3.collidepoint(mpos):
                            answer_click_state = True
                            reset_arrow = True
    
                    if (answer_box != None):
                        mpos = pygame.mouse.get_pos()
                        if arrow_rect.collidepoint(mpos):
                            frames[4], frames[1] = 0, 1

                # Info frame
                if (frames[5] == 1): 
                    mpos = pygame.mouse.get_pos()
                    if arrow_rect.collidepoint(mpos):
                        frames[5], frames[1] = 0, 1
                        init_params = True

            if reset_arrow == True:
                arrow = None
                arrow_rect = None
                reset_arrow = False

            if del_question:
                interact_1 = None
                interact_2 = None
                interact_3 = None
                atextRect = None
                del_question = False
                
    # print(curr_org)        
    # Draws the surface object to the screen.
    pygame.display.update()



