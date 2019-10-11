import json # to work with json file format
from bs4 import BeautifulSoup # to parse html
import pandas as pdgit 

def clean_id_col():
    # pull values(actual ids) from dictionaries
    i = 0
    for i in range(len(df._id)):
        df['_id'][i] = df._id[i].values()
    
    # convert from dict_val to pandas series
    id_series = pd.Series([], name='id')
    for dict_val in df['_id']:
        dict_val = list(dict_val)
        dict_ser = pd.Series([dict_val])
        id_series = pd.concat([id_series,dict_ser], axis=0)
    id_series.reset_index(drop=True, inplace=True)
    
    # convert series of lists to series of strings
    for i in range(len(id_series)):
        id_series[i] = ', '.join(id_series[i])
        
    # drop old, messy id column
    df['id'] = id_series
    df.drop(['_id'], axis=1, inplace=True)