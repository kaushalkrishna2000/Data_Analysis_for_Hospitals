import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.set_option('display.max_columns', 8)
'''                  Data  collect                             '''
general=pd.read_csv('test/general.csv')
prenatal=pd.read_csv('test/prenatal.csv')
sports=pd.read_csv('test/sports.csv')

'''                   Data clump                                '''
prenatal.rename(columns={'HOSPITAL':'hospital','Sex':'gender'},inplace=True)
sports.rename(columns={'Male/female':'gender','Hospital':'hospital'},inplace=True)
df=pd.concat([general,prenatal,sports],axis=0,ignore_index=True)


'''               Data cleaning                  '''
df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.dropna(axis=0,how='all',inplace=True)
df.replace(['male','man'],'m',inplace=True)
df.replace(['female','woman'],'f',inplace=True)
df.loc[(df['hospital']=='prenatal'),'gender']='f'
df.fillna(0,inplace=True)

'''             Answer questions                 '''
a=[]

a.append('general')
a.append(len(df[(df['hospital']=='general')&(df['diagnosis']=='stomach')])/len(df[(df['hospital']=='general')]))
a.append(len(df[(df['hospital']=='sports')&(df['diagnosis']=='dislocation')])/len(df[(df['hospital']=='sports')]))
a.append(abs(df[(df['hospital']=='sports')]['age'].median()-df[(df['hospital']=='general')]['age'].median()))
a.append('prenatal 325')
a[1]=round(a[1],3)
a[2]=round(a[2],3)

'''                     Visualise data                   '''

sns.histplot(data=df['age'])
plt.show()

df.groupby('diagnosis').size().plot(kind='pie', autopct='%.2f')
plt.show()

sns.violinplot(data=df['height'])
plt.show()

'''                    Answer Questions                   '''
a=['15-35','pregnancy',"It's because ....."]
d={1:'st',2:'nd',3:'rd'}
for i in range(3):
    print(f'The answer to the {i+1}{d[i+1]} question: {a[i]}')