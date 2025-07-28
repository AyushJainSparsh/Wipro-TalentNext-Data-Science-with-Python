# Predict the price of the car based on its features. Use appropriate evaluation metrics.  Dataset :  cars.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv('cars.csv')
dataset = dataset.dropna()
dataset.drop(columns=['car name'], inplace=True)
X = dataset.drop(columns=['price'])
y = dataset['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Create a model that can predict  the profit based on its features . Use appropriate evaluation metrics.
# The  Dataset can be downloaded  from kaggle.com   Dataset : 50_startups.csv

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv('50_startups.csv')
dataset = dataset.dropna()
dataset = pd.get_dummies(dataset, drop_first=True)
X = dataset.drop(columns=['Profit'])
y = dataset['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Create a model that can predict  the profit based on its features . Use appropriate evaluation metrics.
# The  Dataset can be downloaded  from kaggle.com   Dataset : Salary_Data

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv('Salary_Data.csv')
dataset = dataset.dropna()
dataset.drop(columns=[['Gender','Education','Job Title']], inplace=True)
X = dataset.drop(columns=['Salary'])
y = dataset['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')