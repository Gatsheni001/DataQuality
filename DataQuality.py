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
# Identify and remove duplicate records
df = df.drop_duplicates()
print(df.duplicated().sum())

#Check for missing value
df['Records Affected'] = df['Records Affected'].replace('Unknown', np.nan)
print("Check for missing values in 'Records Affected':")
print(df['Records Affected'].isnull().sum())

#handle them by filling with the mean value
mean_records_affected = df['Records Affected'].astype(float).mean()
df['Records Affected'] = df['Records Affected'].replace(np.nan, mean_records_affected)
print("Mean value for 'Records Affected':", mean_records_affected)
print(df['Records Affected'].isnull().sum())


#downloading the cleaned data
df.to_csv('dataquality_cleaned.csv', index=False)

# Identify departments where the number of affected records is significantly higher than usual.
department_issues = df.groupby('Department')['Records Affected'].sum()
mean_issues = department_issues.mean()
std_issues = department_issues.std()
outliers = department_issues[department_issues > mean_issues + 2 * std_issues]
print("Departments with significantly higher number of affected records:")
print(outliers)

'''
Complexity of Operations: Departments with more complex operations, such as IT or Finance, may handle a larger volume of data and more intricate data processes, increasing the likelihood of data quality issues.
Data Entry and Management Practices: Departments with less rigorous data entry and management practices may experience more data quality issues. This could be due to insufficient training, lack of standardized procedures, or inadequate data validation mechanisms.
'''

#Find the top 2 departments with the most high-severity issues
high_severity_Department = df[df['Issue Severity'] == 'High']['Department'].value_counts().head(2)
print("Top 2 departments with the most high-severity issues:")
print(high_severity_Department)

#Generate a boxplot to visualize records affected by high-severity issues across departments.
plt.figure(figsize=(10, 6))
df_high_severity = df[df['Issue Severity'] == 'High']
plt.boxplot([df_high_severity[df_high_severity['Department'] == department]['Records Affected'] for department in high_severity_Department.index], labels=high_severity_Department.index)
plt.ylabel('Records Affected')
plt.title('Records Affected by High-Severity Issues Across Departments')
plt.show()


