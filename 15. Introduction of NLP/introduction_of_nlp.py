'''
Perform Text Preprocessing on SMSSpamCollection Dataset. 
The dataset can be downloaded from  https://www.kaggle.com/datasets
'''

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer

dataset = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return ' '.join(tokens)

dataset['message'] = dataset['message'].apply(preprocess_text)
print(dataset.head())