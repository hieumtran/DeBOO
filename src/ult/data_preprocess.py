import pandas as pd

def dup_check(df):
    df_dup = df.iloc[:, 4:].drop_duplicates()
    if len(df_dup) == len(df):
        print('No duplication found')
    else:
        print(len(df_dup))
        print(len(df))
        print(df_dup.index)
        print(df.index)

def drop(df):
    df.drop('Total attributes', axis=1, inplace=True)
    df.drop(23, axis=0, inplace=True)
    df.to_csv('./data/Q_CDI.csv', index=False)

def match_questions(df, question):
    ID_question = df.columns[4:]
    if len(ID_question) == len(question['ID']):
        print('All questions has their ID')
        if (ID_question == question['ID']).all():
            print('All questions ID matches')
        else:
            print(ID_question == question['ID'])
    else:
        print(len(ID_question))
        print(len(question['ID']))
        print(ID_question)
        print(question['ID'])
    
if __name__ == "__main__":
    df = pd.read_csv('./data/Q_CDI.csv')
    question = pd.read_csv('./data/Q_ID.csv')
    # Preprocess data
    # drop(df)
    dup_check(df)
    match_questions(df, question)