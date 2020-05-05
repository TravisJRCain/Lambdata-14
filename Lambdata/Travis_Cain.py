import numpy as np 
import pandas as pd 
print('Hello World')

def obj_jister(df):
    '''
    This function takes in a dataframe and returns a list of columns that contain objects
    '''
    obj_list = []
    for col in df.select_dtypes([np.object]):
        obj_list.append(col)
    return obj_list

def nan_cleaning(df):
    '''
    This function takes in a dataframe and cleans nulls by replacing with 'Unknown.'
    '''
    df = df.replace(np.nan, 'Unknown')
    return df.reset_index(drop=True)
print('Done')
