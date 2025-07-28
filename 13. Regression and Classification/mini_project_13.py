'''
Use Case  :   Sales Prediction
Create a model which will predictthe sales based on campaigning expenses .
Dataset :  Advertising.csv
The dataset can be downloaded from  https://www.kaggle.com/datasets
Perform the following task.
•Load the data in the DataFrame.
•Perform  Data Preprocessing
•Handle Categorical  Data
•Perform Exploratory Data Analysis
•Build the model using Multiple Linear Regression
•Use the appropriate evaluation metrics
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv('Advertising.csv')
x=dataset.drop(['Sales'], axis=1)
y=dataset['Sales']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
score = r2_score(y_test, y_pred)
print(f'R-squared Score: {score}')


'''
Use Case :   Diabetes Prediction
Consider the PIMA Indians diabetes dataset.
Create a Model for diabetes prediction based on the features mentioned in the dataset.
Dataset :  PIMA Indians diabetes dataset.
The dataset can be downloaded from  https://www.kaggle.com/datasets
Perform the following tasks.
•Load the data in the DataFrame.
•Perform  Data Preprocessing
•Perform Exploratory Data Analysis
•Build the model using Logistic Regression and K-Nearest Neighbour
•Use the appropriate evaluation metrics
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

dataset = pd.read_csv('Diabetes_prediction.csv')
x=dataset.drop(['Diagnosis'], axis=1)
y=dataset['Diagnosis']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_report(y_test, y_pred)}')
