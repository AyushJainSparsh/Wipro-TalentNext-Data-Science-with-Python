# Perform Exploratory Data Analysis for the dataset Mall_Customers. 
# The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mall_Customers.csv')

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True, color='skyblue')
plt.title('Age Distribution')

plt.subplot(1, 3, 2)
sns.histplot(df['Annual Income (k$)'], kde=True, color='salmon')
plt.title('Annual Income Distribution')

plt.subplot(1, 3, 3)
sns.histplot(df['Spending Score (1-100)'], kde=True, color='lime')
plt.title('Spending Score Distribution')

plt.tight_layout()
plt.show()

plt.figure(figsize=(5,4))
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

plt.figure(figsize=(7,6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='Set1', data=df)
plt.title('Customer Segmentation')
plt.show()


# Perform Exploratory Data Analysis for the dataset  salary_data. 
# The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Salary_Data.csv')

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
sns.histplot(df['YearsExperience'], kde=True, color='skyblue')
plt.title('Years of Experience Distribution')

plt.subplot(1, 2, 2)
sns.histplot(df['Salary'], kde=True, color='salmon')
plt.title('Salary Distribution')

plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
sns.scatterplot(x='YearsExperience', y='Salary', data=df, color='purple')
plt.title('Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

print("\n--- Correlation Matrix ---")
print(df.corr())

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

# Perform Exploratory Data Analysis for the dataset  Social Network Ads. 
# The dataset can be downloaded from  https://www.kaggle.com/datasets

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv')
print(df.info())
print(df.describe())
print(df.isnull().sum())

sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

sns.countplot(x='Purchased', data=df)
plt.title('Purchase Decision Distribution')
plt.show()

sns.histplot(df['Age'], kde=True, color='skyblue')
plt.title('Age Distribution')
plt.show()

sns.histplot(df['EstimatedSalary'], kde=True, color='salmon')
plt.title('Estimated Salary Distribution')
plt.show()

sns.boxplot(x='Purchased', y='Age', data=df)
plt.title('Age vs Purchase')
plt.show()

sns.boxplot(x='Purchased', y='EstimatedSalary', data=df)
plt.title('Salary vs Purchase')
plt.show()

print(df.corr())
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()