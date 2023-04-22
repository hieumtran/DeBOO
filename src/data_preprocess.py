import pandas as pd

def dup_check(df):
    df_dup = df.iloc[:, 4:].drop_duplicates()
    print(len(df_dup))
    print(len(df))
    print(df_dup.index)
    print(df.index)
    print(len(df_dup) == len(df))

def drop(df):
    df.drop('Total attributes', axis=1, inplace=True)
    df.drop(23, axis=0, inplace=True)
    df.to_csv('./data/Q_CDI.csv', index=False)
    
if __name__ == "__main__":
    df = pd.read_csv('./data/Q_CDI.csv')

    # Preprocess data
    # drop(df)
    dup_check(df)