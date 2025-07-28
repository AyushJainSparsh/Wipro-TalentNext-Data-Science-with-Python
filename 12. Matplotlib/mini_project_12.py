'''
Use Case  :   Diabetes Prediction 
Perform Exploratory Data Analysis for the Diabetes Dataset.
Dataset :  Diabetes.csv
The dataset can be downloaded from  https://www.kaggle.com/datasets
Perform the following tasks
1.Load the data in the DataFrame
2.Data Pre-processing
3.Handle the Categorical Data
4.Perform Uni-variate Analysis 
5.Perform Bi-variate Analysis
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Diabetes.csv')
print(df.head())
print(df.info())

print(df.isnull().sum())

cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols_with_zero] = df[cols_with_zero].replace(0, pd.NA)

df.fillna(df.median(), inplace=True)

print("\n--- Univariate Analysis ---")

df.hist(figsize=(12, 10), bins=20, color='skyblue')
plt.suptitle('Feature Distributions')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df)
plt.title('Boxplot of Features')
plt.xticks(rotation=45)
plt.show()

print("\n--- Bivariate Analysis ---")

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

features = ['Glucose', 'BMI', 'Age', 'Insulin']
for feature in features:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='Outcome', y=feature, data=df)
    plt.title(f'{feature} vs Outcome')
    plt.show()