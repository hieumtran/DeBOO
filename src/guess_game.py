import pandas as pd
import numpy as np
import time
from thefuzz import fuzz
from thefuzz import process

def sample_questions(game_question, read_question):
    # for i in range(len(game_question)):
    if len(game_question) > 1:
        ask_question = np.random.choice(game_question, size=2, replace=False)
        print('Choose a question below:')
        for i in range(len(ask_question)):
            print(f"{i+1}.{read_question.loc[ask_question[i], 'Questions']}")
    
        tmp = int(input('Press 1 or 2:'))
        if tmp == 1:
            return ask_question[0]
        elif tmp == 2:
            return ask_question[1]
        else: 
            raise 'Error Incorrect input'
    elif len(game_question) == 1:
        ask_question = game_question[0]
        print('There are no more questions after this:')
        print(read_question.loc[ask_question[i], 'Questions'])
        return ask_question
    else:
        raise 'No more question.'
        
def response(value):
    correct_answer = ['Yes, absolutely', 'Yup!', 'Yes, good question!',
                      'I think so', 'I guess so', 'I am not entirely sure, but probably yes.']
    incorrect_answer = ['No, nahhh!', 'Nope!', 'No, try another one!',
                        "I don't think so", 'I guess not', 'I am not sure, but very likely no.']
    if value == 1:
        ans = np.random.choice(correct_answer, size=1, replace=False)[0]
    elif value == 0:
        ans = np.random.choice(incorrect_answer, size=1, replace=False)[0]
    print('Hmmmmm....')
    time.sleep(np.random.choice([1,2,3], size=1, replace=False)[0])
    print(ans)

def score(total, num_question, ratio_correct):
    return (total - num_question) * ratio_correct

if __name__ == "__main__":
    df = pd.read_csv('./data/Q_CDI.csv')
    read_question = pd.read_csv('./data/Q_ID.csv')
    read_question = read_question.set_index('ID')

    org = df['Organization']

    while True:
        curr_org = np.random.choice(org, size=1, replace=False)[0]
        goal = df.loc[df['Organization'] == curr_org].iloc[:, 4:]
        question = df.columns[4:].to_list()
        game_question = df.columns[4:].to_list()
        print(curr_org)
        num_question = 0
        while len(game_question) != 0:
            choice = int(input('Choose 1 for questions and 2 for guess:'))
            if choice == 1:
                num_question += 1
                # Given the question
                sample_quest = sample_questions(game_question, read_question)

                # Print the question
                value = goal.loc[:, sample_quest].values[0]
                response(value)

                # Pop old questions
                game_question.remove(sample_quest)
            elif choice == 2:
                guess = input('Input your answer: ')
                ratio_correct = fuzz.ratio(guess, curr_org) / 100
                print(ratio_correct)
                if ratio_correct == 1:
                    print('Perfect! I knew you could do it')
                if ratio_correct < 1 and ratio_correct >= 60:
                    print("Outstanding! I knew you could do it!")
                if ratio_correct < 60 and ratio_correct >= 40:
                    print("Not bad!  I couldn't have done it better!")
                if ratio_correct < 40:
                    print("Nice try! But you gotta be better next time")
                
                if ratio_correct != 1:
                    print(f'Your answer matches {ratio_correct*100}% with our answer. \n The correct answer is: ', curr_org)
            
                score = score(len(question), num_question, ratio_correct)
                print(f'Your score is: {score}')
                break
        
        not_or_continue = int(input('Do you wanna continue?'))

        if not_or_continue == 1:
            continue
        elif not_or_continue == 0:
            break
                