'''
Create a model that will predictthe ratingbased on the feedbackof the customer.
Feature:  Text
Label: Stars
Dataset:yelp.csv
The dataset can be downloaded from   https://www.kaggle.com/datasets
'''

# features = business_id,date,review_id,stars,text,type,user_id,cool,useful,funny

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score

dataset = pd.read_csv('yelp.csv')
dataset = dataset[['text', 'stars']].dropna()
dataset['stars'] = dataset['stars'].astype(str)  
X = dataset['text']
y = dataset['stars']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = make_pipeline(CountVectorizer(), MultinomialNB()) 
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))