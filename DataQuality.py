import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dataquality.csv')
print(df.head())

# Display summary statistics for numerical variables
print(df.describe())

# Identify and list the top 3 departments with the most data quality issues.
print(df['Department'].value_counts().head(3))

# Find which data source has the highest number of high-severity issues.
print(df[df['Issue Severity'] == 'High']['Data Source'].value_counts().head(1))

# Generate a bar chart visualizing the count of different data quality issues.
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
df['Data Quality Issue'].value_counts().plot(kind='bar')
size = len(df['Data Quality Issue'].value_counts())
plt.xticks(range(size), df['Data Quality Issue'].value_counts().index, rotation=90)
plt.tight_layout()  # Adjust layout to ensure everything fits without overlap
plt.show()

'''
Inaccurate Insights: Poor data quality can lead to incorrect analysis and insights. Decisions based on inaccurate data can result in misguided strategies and actions.
Reduced Efficiency: Data quality issues often require additional time and resources to clean and validate data, reducing overall efficiency and productivity.
Loss of Trust: Consistent data quality problems can erode trust in the data and the systems that produce it, leading to skepticism and reluctance to rely on data-driven decisions.
'''

#Data Cleaning
#Identify and Removes duplicates
df.drop_duplicates(inplace=True)

#downloading the cleaned data
df.to_csv('dataquality_cleaned.csv', index=False)


