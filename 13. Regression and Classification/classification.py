# Create a model that can predict the disease of cancer based on features given in the dataset. 
# Use appropriate evaluation metrics.  Dataset : cancer.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv('cancer.csv')
dataset.drop(columns=['Gender'], inplace=True)
coder = OneHotEncoder()
y = coder.fit_transform(dataset[['CANCER']])
x = dataset.drop(['CANCER'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
conf_matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_report(y_test.argmax(axis=1), y_pred.argmax(axis=1))}')


# Create a model that can predict that the customer has purchased item or not based on features 
# given in the dataset. Use appropriate evaluation metrics.  Dataset : Social_Ntetwork_Ads.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.drop(['Purchased'], axis=1)
y = dataset['Purchased']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_report(y_test, y_pred)}')