import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('pisa2012_filtered_clean.csv')
df.rename({'CNT': 'Country Code', 'ST03Q02': 'Birth Year', 'ST04Q01': 'Gender',
           'STUDREL': 'Teacher Student Relations', 'TCHBEHFA': 'Teacher Behavior',
           'COBN_S': 'Birth Country', 'COBN_M': 'Birth Country of Mother',
           'COBN_F': 'Birth Country of Father',
           'EXAPPLM': 'Experience with Applied Math in School',
           'EXPUREM': 'Experience with Pure Math in School',
           'avg Science Score': 'Average Science Score',
           'Avg Math Score': 'Average Math Score',
           'Avg Reading Score': 'Average Reading Score',
           'WEALTH': 'Wealth'}, axis='columns', inplace=True)
df.info()
print(df.head())

# df.to_csv('pisa2012_filtered_clean_titled.csv')
