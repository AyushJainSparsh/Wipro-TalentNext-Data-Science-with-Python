'''
Use Case:Perform   the   Outlier   detection   for   the   given dataset   i.e.datasetExample
Dataset :    datasetExample.csv
Perform the following task
•Load the data in the DataFrame.
•Detection of Outliers
'''

import pandas as pd
import numpy as np

dataset = pd.read_csv('datasetExample.csv')

q1 = dataset.quantile(0.25)
q3 = dataset.quantile(0.75)
iqr = q3 - q1
outlier_condition = (dataset < (q1 - 1.5 * iqr)) | (dataset > (q3 + 1.5 * iqr))
outliers = dataset[outlier_condition.any(axis=1)]
print("Outliers detected:")
print(outliers)