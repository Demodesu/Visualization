#https://data.go.th/dataset/covid-19-daily

import pandas as pd
import os

os.chdir("E:\Gun's stuff\Machine Learning\covid visualization")

df = pd.read_excel('covid-cases-thailand.xlsx', sheet_name='Test Data')

df = df.drop(['No.','announce_date','Notified date','province_of_onset','district_of_onset','Unit','nationality','province_of_isolation','risk'],axis='columns')

print(df.head(5))

print(df.columns[df.isna().any()])
print(df.isna().sum())

df = df.dropna()
df = df.reset_index(drop=True)

print(df.columns[df.isna().any()])

df['sex'] = df['sex'].replace(['ชาย'],'0') #0 = male
df['sex'] = df['sex'].replace(['หญิง'],'1') #1 = female

from matplotlib import pyplot as plt

df.hist(column='age',bins=25)
plt.show()



