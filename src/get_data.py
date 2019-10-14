import json # to work with json file format
from bs4 import BeautifulSoup # to parse html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_json('data/bigfoot_data.json', lines = True)

cols = ['SUBMITTED', 'TITLE', 'YEAR', 'SEASON', 'MONTH',
                                  'STATE', 'COUNTY', 'LOCATION DETAILS', 'NEAREST TOWN',
                                  'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED',
                                  'OTHER WITNESSES', 'OTHER STORIES', 'TIME AND CONDITIONS',
                                  'ENVIRONMENT']

# save this for later
# for i, col in enumerate(cols):
#     cols[i] = col.lower()

html_df = pd.DataFrame(columns = cols)
html_df

for doc in df.html:
    doc_dict = dict()
    souped_doc = BeautifulSoup(doc, 'html.parser')
    spans = souped_doc.find_all('span', {'class': 'field'})
    
    try:
        doc_dict['SUBMITTED'] = spans[0].text
        doc_dict['TITLE'] = spans[1].text
    except:
        continue
        
    for sentence in souped_doc.find_all("p"):
        if any(span in sentence for span in spans):
            text = sentence.text
            #print (text)
            #print('------\n')
            list_info = text.split(': ',1)
            #print(list_info)
            doc_dict[list_info[0]] = list_info[1]
    
    html_df = html_df.append({k:doc_dict[k] for k in cols if k in doc_dict}, ignore_index=True)
    
newcols = []

for col in html_df.columns:
    newcols.append(col.lower())
    
html_df.columns = newcols